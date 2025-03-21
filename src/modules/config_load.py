import os
import configparser
import importlib.util
import subprocess
import sys

CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..', 'config', '.config')

def check_and_install(package_name):
    """Check if a package is installed, and prompt the user to install it if not."""
    if importlib.util.find_spec(package_name) is None:
        print(f"The required library '{package_name}' is not installed.")
        response = input(f"Do you want to install '{package_name}' now? (y/n): ").strip().lower()
        if response == 'y':
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
                print(f"'{package_name}' has been installed successfully.")
            except subprocess.CalledProcessError:
                print(f"Failed to install '{package_name}'. Please install it manually.")
        else:
            print(f"Please install '{package_name}' manually using 'pip install {package_name}'.")

def load_config():
    """Load the configuration from the .config file."""
    # Check for required libraries
    check_and_install('configparser')  # Example: Ensure configparser is installed

    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        print("Configuration file not found. Creating a new one.")
        
        # Prompt for the save location
        default_save_location = os.path.expanduser("~/OSI_VADR")
        save_location = input(f"Enter the save location for artifacts (default: {default_save_location}): ").strip()
        if not save_location:
            save_location = default_save_location
        os.makedirs(save_location, exist_ok=True)

        # Prompt for the DNS lookup tool
        print("Select the DNS lookup tool:")
        print("1. DNSDUMPSTER")
        print("2. WHOIS")
        dns_lookup_tool = None
        while dns_lookup_tool not in ['1', '2']:
            dns_lookup_tool = input("Enter 1 or 2: ").strip()
            if dns_lookup_tool not in ['1', '2']:
                print("Invalid selection. Please enter 1 or 2.")
        dns_lookup_tool = "DNSDUMPSTER" if dns_lookup_tool == '1' else "WHOIS"

        # Prompt for the API key based on the selected tool
        if dns_lookup_tool == "DNSDUMPSTER":
            api_key = input("Enter your DNSDumpster API key: ").strip()
        elif dns_lookup_tool == "WHOIS":
            api_key = input("Enter your WHOIS API key: ").strip()

        # Write the configuration to the .config file
        config['SETTINGS'] = {
            'SAVE_LOCATION': save_location,
            'DNS_LOOKUP_TOOL': dns_lookup_tool,
            'DNS_LOOKUP_API_KEY': api_key
        }
        config['API_KEYS'] = {'SHODAN_API_KEY': input("Enter your Shodan API key: ").strip()}
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
        print(f"Configuration saved to {CONFIG_FILE}")
    else:
        # Load the .config file
        config.read(CONFIG_FILE)
    return config

def get_save_location():
    """Retrieve the save location for artifacts from the configuration."""
    config = load_config()
    return config.get('SETTINGS', 'SAVE_LOCATION', fallback=os.path.expanduser("~/OSI_VADR"))

def get_api_key():
    """Retrieve the Shodan API key from the configuration."""
    config = load_config()
    return config.get('API_KEYS', 'SHODAN_API_KEY', fallback=None)

def get_dns_lookup_tool():
    """Retrieve the DNS lookup tool from the configuration."""
    config = load_config()
    return config.get('SETTINGS', 'DNS_LOOKUP_TOOL', fallback="DNSDUMPSTER")

def get_dns_lookup_api_key():
    """Retrieve the API key for the selected DNS lookup tool."""
    config = load_config()
    return config.get('SETTINGS', 'DNS_LOOKUP_API_KEY', fallback=None)

def get_shodan_api_key():
    """Retrieve the Shodan API key from the configuration."""
    config = load_config()
    return config.get('API_KEYS', 'SHODAN_API_KEY', fallback=None)

def get_config_value(key, default=None):
    """
    Retrieve a configuration value from the .config file.
    :param key: The key to look up in the configuration.
    :param default: The default value to return if the key is not found.
    :return: The value of the key, or the default value if not found.
    """
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), '..', '..', '.config')

    if not os.path.exists(config_file):
        print(f"Config file not found: {config_file}")
        return default

    config.read(config_file)

    # Assuming the config file has a [DEFAULT] section
    return config['DEFAULT'].get(key, default)