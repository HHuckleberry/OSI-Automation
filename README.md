# OSINT Automation Project

This project is designed to automate Open Source Intelligence (OSINT) tasks, focusing on identifying target organizations, enumerating DNS points, validating sites, conducting deep Google searches for sensitive keywords, and scraping relevant documents and contact information from their websites.

## Project Structure

```
osint-automation
├── src
│   ├── main.py                # Entry point of the application
│   ├── modules                # Contains various modules for OSINT tasks
│   │   ├── target_identification.py  # Functions for identifying target organizations
│   │   ├── dns_enumeration.py       # Functions for DNS enumeration
│   │   ├── site_validation.py        # Functions for site validation
│   │   ├── google_search.py          # Functions for conducting Google searches
│   │   └── web_scraping.py           # Functions for web scraping tasks
│   ├── utils                   # Utility functions for the application
│   │   ├── http_client.py      # HTTP request handling
│   │   ├── parser.py           # Data parsing functions
│   │   └── logger.py           # Logging management
│   └── config                  # Configuration settings
│       └── settings.py         # Application settings
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files to ignore in version control
├── README.md                   # Project documentation
└── LICENSE                     # Licensing information
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/HHuckleberry/OSI-Automation
   cd osint-automation
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the OSINT automation process, execute the following command:
```
python src/main.py
```

## Features

- **Target Identification**: Identify target organizations and retrieve their URLs.
- **DNS Enumeration**: Enumerate DNS points using DNSDumpster and common name lists.
- **Site Validation**: Validate the availability and security of identified sites.
- **Google Search**: Conduct deep searches for sensitive keywords related to the target organization.
- **Web Scraping**: Scrape documents and contact information from validated websites.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.