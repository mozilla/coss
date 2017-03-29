#!/usr/bin/env bash
echo "running startup..."

# Make Django migrations, just in case.
python manage.py makemigrations

# Then migrate up, again just in case.
python manage.py migrate

# Gather the static assets...
python manage.py collectstatic --no-input

# Finally, start up the system.
python manage.py runserver "0.0.0.0:$PORT"
