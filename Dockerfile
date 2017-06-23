FROM python:3.5

EXPOSE 8000
COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt
CMD python manage.py migrate --noinput &&\
    python manage.py collectstatic --noinput &&\
    python manage.py runserver 0.0.0.0:8000
