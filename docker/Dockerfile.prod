FROM python:3-slim

EXPOSE 8000
WORKDIR /code
CMD ["./bin/run-prod.sh"]

RUN adduser --uid 431 --disabled-password --disabled-login --gecos 'webdev' --no-create-home webdev

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential ruby-sass && \
    rm -rf /var/lib/apt/lists/*

COPY requirements /code/requirements/
RUN pip install --require-hashes --no-deps -r requirements/prod.txt
COPY . /code

RUN chown webdev.webdev -R .
USER webdev
RUN bin/bootstrap.sh
