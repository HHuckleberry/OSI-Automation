import requests
from requests.exceptions import RequestException

def get_request(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
    except RequestException as e:
        print(f"HTTP GET request failed: {e}")
        return None

def post_request(url, data=None, headers=None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
    except RequestException as e:
        print(f"HTTP POST request failed: {e}")
        return None