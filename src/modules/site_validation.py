def validate_site(url):
    import requests

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            # Check if the site uses HTTPS
            if url.startswith("https://"):
                return {"url": url, "status": "valid", "secure": True}
            else:
                return {"url": url, "status": "valid", "secure": False}
        else:
            return {"url": url, "status": "invalid", "secure": None}
    except requests.RequestException:
        return {"url": url, "status": "invalid", "secure": None}