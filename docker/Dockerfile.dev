FROM python:3

EXPOSE 8000
WORKDIR /app
CMD ["./bin/run-dev.sh"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential ruby-sass && \
    rm -rf /var/lib/apt/lists/*

COPY requirements /app/requirements/
RUN pip install --no-cache-dir --require-hashes --no-deps -r requirements/dev.txt
