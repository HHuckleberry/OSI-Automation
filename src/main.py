import sys
import argparse
import dns.resolver
from modules.config_load import load_config
from modules.target_identification import get_target_url
from modules.dns_enumeration import enumerate_common_dns, enumerate_dns
from modules.site_validation import validate_site
from modules.google_search import perform_google_search
from modules.web_scraping import scrape_documents, scrape_contact_info

# Load the configuration
print("Loading configuration...")
config = load_config()
print("Configuration loaded successfully.")

def main(target_name):
    
    print(f"Configuration loaded successfully: {config.sections()}")

    # Block 1 - DNS Enumeration API
    print(f"Identifying target for: {target_name}")
    target_url = get_target_url(target_name)
    
    if not target_url:
        print("Target URL could not be identified.")
        sys.exit(1)

    print(f"Target URL identified: {target_url}")
    
    print("Enumerating DNS points...")
    dns_records = enumerate_dns(target_name)
    #Next set- dns querys
    print("Enumerating DNS points...")
    dns_records = enumerate_dns(target_name)
    
    print(f"DNS Records: {dns_records}")
    
    print("Enumerating common DNS records...")
    common_dns_records = enumerate_common_dns(target_name)
    print(f"Common DNS Records: {common_dns_records}")
    
    print("Validating sites...")
    valid_sites = [site for site in dns_records if validate_site(site)]
    

    print(f"DNS Records: {dns_records}")



    print("Validating sites...")
    valid_sites = [site for site in dns_records if validate_site(site)]
    
    if not valid_sites:
        print("No valid sites found.")
        sys.exit(1)




    print(f"Valid sites: {valid_sites}")
    
    print("Conducting Google searches for sensitive keywords...")
    sensitive_keywords = ['SCADA', 'HMI', 'OT', 'ICS'] # change to grab from SENSITIVE_KEYWORDS
    search_results = {}
    
    for keyword in sensitive_keywords:
        search_results[keyword] = perform_google_search(target_name, keyword)
    
    print("Search results:")
    for keyword, results in search_results.items():
        print(f"{keyword}: {results}")
    
    print("Scraping documents and contact information from valid sites...")
    for site in valid_sites:
        documents = scrape_documents(site)
        contact_info = scrape_contact_info(site)
        print(f"Documents from {site}: {documents}")
        print(f"Contact info from {site}: {contact_info}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSINT Automation Tool")
    parser.add_argument("--target", help="The target organization or website name")
    args = parser.parse_args()

    # If --target is not provided, prompt the user for input
    if not args.target:
        target_name = input("Please enter the target organization or website name: ").strip()
    else:
        target_name = args.target

    main(target_name)