from factories.fetcher_factory import FetcherFactory
from factories.metadata_factory import MetadataFactory

class Fetcher:
    def __init__(self, urls, include_metadata=False):
        self.urls = urls
        self.include_metadata = include_metadata

    def fetch(self):
        fetcher_factory = FetcherFactory()
        metadata_factory = MetadataFactory()

        for url in self.urls:
            fetcher = fetcher_factory.create_fetcher(url)
            result = fetcher.fetch()

            if self.include_metadata:
                metadata = metadata_factory.create_metadata(url, result)
                if metadata:
                    metadata.save()
                else:
                    print(f"Error: Failed to create metadata for {url}.")
