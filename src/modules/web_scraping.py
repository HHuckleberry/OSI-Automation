import requests
from bs4 import BeautifulSoup
import re

def scrape_documents(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        documents = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.search(r'\.(pdf|docx?|pptx?)$', href, re.IGNORECASE):
                documents.append(href if href.startswith('http') else url + href)
        
        return documents
    except requests.RequestException as e:
        print(f"Error scraping documents from {url}: {e}")
        return []

def scrape_contact_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        contact_info = {}
        
        # Example of scraping email addresses
        emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.text))
        if emails:
            contact_info['emails'] = list(emails)
        
        # Example of scraping phone numbers
        phones = set(re.findall(r'\+?\d[\d -]{8,}\d', soup.text))
        if phones:
            contact_info['phones'] = list(phones)
        
        return contact_info
    except requests.RequestException as e:
        print(f"Error scraping contact info from {url}: {e}")
        return {}