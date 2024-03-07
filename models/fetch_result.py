from bs4 import BeautifulSoup
import requests


class FetchResult:
    def __init__(self, url, content=None, num_links=None, num_images=None, last_fetch=None):
        self.url = url
        self.content = content
        self.num_links = num_links
        self.num_images = num_images
        self.last_fetch = last_fetch

    def fetch(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.content = BeautifulSoup(response.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            self.content = None
