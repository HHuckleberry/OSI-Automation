import requests
from bs4 import BeautifulSoup
import time

def perform_google_search(query, num_results=10):
    search_url = "https://www.google.com/search"
    params = {
        'q': query,
        'num': num_results,
        'hl': 'en'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(search_url, params=params, headers=headers)
    
    if response.status_code == 200:
        return parse_search_results(response.text)
    else:
        return []

def parse_search_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    
    for g in soup.find_all('div', class_='g'):
        title = g.find('h3').text if g.find('h3') else None
        link = g.find('a')['href'] if g.find('a') else None
        snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else None
        
        if title and link:
            results.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })
    
    return results

def main():
    keywords = ["SCADA", "HMI", "OT", "ICS"]
    for keyword in keywords:
        print(f"Searching for: {keyword}")
        results = perform_google_search(keyword)
        for result in results:
            print(result)
        time.sleep(2)  # Be polite and avoid hitting the server too hard

if __name__ == "__main__":
    main()