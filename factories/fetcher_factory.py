import requests

class FetcherFactory:
    @staticmethod
    def create_fetcher(url):
        return Fetcher(url)

class Fetcher:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return None
