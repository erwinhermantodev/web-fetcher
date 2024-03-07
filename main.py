import os
import sys
from factories.fetcher_factory import FetcherFactory
from factories.metadata_factory import MetadataFactory

def save_html(content, url):
    filename = url.split("//")[-1].split("/")[0]
    with open(f"{filename}.html", "wb") as f:
        f.write(content)
    print(f"Saved {url} as {filename}.html")

def save_metadata(url, metadata):
    filename = url.split("//")[-1].split("/")[0]
    with open(f"{filename}_metadata.txt", "w") as f:
        f.write(f"site: {url}\n")
        f.write(f"num_links: {metadata.num_links}\n")
        f.write(f"num_images: {metadata.num_images}\n")
        f.write(f"last_fetch: {metadata.last_fetch}\n")
    print(f"Metadata for {url} saved.")

def main():
    if len(sys.argv) < 2:
        print("Usage: ./fetch [--metadata] <url1> <url2> ...")
        sys.exit(1)

    urls = sys.argv[2:]  # Exclude the first argument (script name) and optional flag
    include_metadata = "--metadata" in sys.argv
    for url in urls:
        fetcher = FetcherFactory.create_fetcher(url)
        content = fetcher.fetch()
        if content:
            save_html(content, url)
            if include_metadata:
                metadata = MetadataFactory.create_metadata(content)
                save_metadata(url, metadata)

if __name__ == "__main__":
    main()
