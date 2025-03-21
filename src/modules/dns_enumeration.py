import os
import json
import requests
from datetime import datetime
from modules.config_load import get_dns_lookup_tool, get_dns_lookup_api_key, get_save_location

def enumerate_dns(target_name):
    """Enumerate DNS records using the selected tool."""
    dns_tool = get_dns_lookup_tool()
    api_key = get_dns_lookup_api_key()
    print(f"Using DNS lookup tool: {dns_tool}")
    
    if dns_tool == "DNSDUMPSTER":
        return enumerate_with_dnsdumpster(target_name, api_key)
    elif dns_tool == "WHOIS":
        return enumerate_with_whois(target_name, api_key)
    else:
        raise ValueError(f"Unsupported DNS lookup tool: {dns_tool}")

def enumerate_with_dnsdumpster(target_name, api_key):
    """Perform DNS enumeration using DNSDumpster."""
    print(f"Enumerating DNS records for {target_name} using DNSDumpster with API key...")
    headers = {"X-API-Key": api_key}
    api_url = f"https://api.dnsdumpster.com/domain/{target_name}"

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON response

        # Save the artifacts
        save_location = get_save_location()
        target_folder = os.path.join(save_location, target_name)
        os.makedirs(target_folder, exist_ok=True)

        # Generate a dynamic filename with target name, tool, and timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        artifact_filename = f"{target_name}-dnsdumpster-{timestamp}.json"
        artifact_path = os.path.join(target_folder, artifact_filename)

        # Save the DNSDumpster results to the file
        with open(artifact_path, 'w') as artifact_file:
            json.dump(data, artifact_file, indent=4)
        print(f"DNSDumpster results saved to {artifact_path}")

        # Extract DNS records
        dns_records = {
            "a": [],
            "cname": [],
            "mx": [],
            "ns": [],
            "txt": []
        }

        for record in data.get("a", []):
            dns_records["a"].append({
                "host": record["host"],
                "ips": [ip["ip"] for ip in record.get("ips", [])]
            })

        dns_records["cname"] = data.get("cname", [])
        dns_records["mx"] = data.get("mx", [])
        for record in data.get("ns", []):
            dns_records["ns"].append({
                "host": record["host"],
                "ips": [ip["ip"] for ip in record.get("ips", [])]
            })
        dns_records["txt"] = data.get("txt", [])

        return dns_records
    except requests.exceptions.RequestException as e:
        print(f"Error using DNSDumpster API: {e}")
        return {}

def enumerate_with_whois(target_url, api_key):
    """Perform DNS enumeration using WHOIS."""
    print(f"Enumerating DNS records for {target_url} using WHOIS with API key {api_key}...")
    return ["whois1.example.com", "whois2.example.com"]

def load_subdomain_wordlist(filepath):
    """Load subdomains from a wordlist file."""
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Wordlist file not found: {filepath}")
        return []

def common_name_list():
    """
    Returns a list of common subdomains to check for a given domain.
    If a custom wordlist is specified in the configuration, it will be loaded.
    Otherwise, a default list is used.
    """
    from modules.config_load import get_config_value  # Assuming this function retrieves config values

    # Check if a custom wordlist is specified in the config
    wordlist_path = get_config_value("DNS_BRUTE_LIST")
    if wordlist_path:
        print(f"Loading subdomain wordlist from: {wordlist_path}")
        return load_subdomain_wordlist(wordlist_path)

    # Default list of subdomains if no wordlist is specified
    print("No custom wordlist specified. Using default subdomain list.")
    return [
        "ftp",
        "rdp",
        "remote",
        "scada",
        "test",
        "admin",
        "wwtp",
        "wtp"
    ]

import dns.resolver

def enumerate_common_dns(domain):
    """
    Enumerate common DNS records for a given domain using dnspython.
    This function performs DNS lookups for common subdomains.
    """
    records = []
    for subdomain in common_name_list():
        full_domain = f"{subdomain}.{domain}"
        print(f"Looking up DNS records for {full_domain}...")
        try:
            dns_record = {}
            # Query A records
            a_records = dns.resolver.resolve(full_domain, 'A', raise_on_no_answer=False)
            dns_record["a"] = [r.to_text() for r in a_records]
            
            # Query CNAME records
            cname_records = dns.resolver.resolve(full_domain, 'CNAME', raise_on_no_answer=False)
            dns_record["cname"] = [r.to_text() for r in cname_records]
            
            # Query MX records
            mx_records = dns.resolver.resolve(full_domain, 'MX', raise_on_no_answer=False)
            dns_record["mx"] = [r.to_text() for r in mx_records]
            
            # Query NS records
            ns_records = dns.resolver.resolve(full_domain, 'NS', raise_on_no_answer=False)
            dns_record["ns"] = [r.to_text() for r in ns_records]
            
            # Query TXT records
            txt_records = dns.resolver.resolve(full_domain, 'TXT', raise_on_no_answer=False)
            dns_record["txt"] = [r.to_text().strip('"') for r in txt_records]
            
            records.append({full_domain: dns_record})
        except dns.resolver.NoAnswer:
            print(f"No DNS records found for {full_domain}.")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {full_domain} does not exist.")
        except Exception as e:
            print(f"Error looking up {full_domain}: {e}")
    return records