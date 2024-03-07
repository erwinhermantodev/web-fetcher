.PHONY: run

run:
    docker run web-fetcher python /app/web-fetcher/main.py $(ARGS)

run-metadata:
    docker run web-fetcher python /app/web-fetcher/main.py --metadata $(ARGS)
