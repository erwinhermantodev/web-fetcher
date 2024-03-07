# Running the Web Fetcher App

## 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone web-fetcher
```

Replace `<repository-url>` with the actual URL of the repository. If you're using GitHub, the URL will typically look like `https://github.com/erwinhermantodev/web-fetcher.git`.

Navigate to the directory of the cloned repository:

```bash
cd <repository-directory>
```

## 2. Build the Docker Image

Next, build the Docker image using the provided Dockerfile. Make sure you have Docker installed on your machine.

```bash
docker build -t web-fetcher .
```

This command will build the Docker image with the tag `web-fetcher`.

## 3. Fetch URLs

Now, you can use the Docker image to fetch URLs. There are two options:

### Option 1: Fetch URLs with Metadata

To fetch URLs along with metadata such as number of links, number of images, and last fetch time:

```bash
docker run --rm -v $(pwd):/app web-fetcher python /app/main.py --metadata "https://www.google.com" "https://autify.com"
```

Replace `"https://www.google.com" "https://autify.com"` with the URLs you want to fetch.

### Option 2: Fetch URLs Only

To fetch URLs without metadata:

```bash

docker run --rm -v $(pwd):/app web-fetcher python /app/main.py "https://www.google.com" "https://autify.com"

```
