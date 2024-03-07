.PHONY: fetch-metadata fetch-only

DOCKER_RUN=docker run --rm -v $(PWD):/app web-fetcher python /app/main.py

fetch-metadata:
	$(DOCKER_RUN) $(URLS) --metadata

fetch-only:
	$(DOCKER_RUN) $(URLS)
