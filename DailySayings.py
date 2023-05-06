import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_arguments():
    parser = argparse.ArgumentParser(description="Website Enumeration Tool")
    parser.add_argument("url", help="URL of the target website")
    return parser.parse_args()

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve the page: {e}")
        return None

def find_links(html_content, base_url):
    links = set()
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        absolute_url = urljoin(base_url, href)
        links.add(absolute_url)
    return links

def enumerate_website(url):
    html_content = make_request(url)
    if html_content:
        links = find_links(html_content, url)
        print(f"Links found on {url}:")
        for link in links:
            print(link)
# main function
if __name__ == "__main__":
    args = parse_arguments()
    url = args.url
    enumerate_website(url)