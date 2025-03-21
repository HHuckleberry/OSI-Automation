def parse_html(html_content):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def parse_json(json_content):
    import json

    return json.loads(json_content)