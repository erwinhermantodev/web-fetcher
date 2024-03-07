from bs4 import BeautifulSoup
from datetime import datetime

class MetadataFactory:
    @staticmethod
    def create_metadata(content):
        soup = BeautifulSoup(content, "html.parser")
        num_links = len(soup.find_all("a"))
        num_images = len(soup.find_all("img"))
        last_fetch = datetime.utcnow().strftime("%a %b %d %Y %H:%M UTC")
        return Metadata(num_links, num_images, last_fetch)

class Metadata:
    def __init__(self, num_links, num_images, last_fetch):
        self.num_links = num_links
        self.num_images = num_images
        self.last_fetch = last_fetch
