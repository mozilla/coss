#!/usr/bin/env bash
echo "running startup..."

# This is really funny, but necessary
cd cmstest

# Make Django migrations, just in case.
python manage.py makemigrations

# Then migrate up, again just in case.
python manage.py migrate

# Finally, start up the system.
python manage.py runserver "0.0.0.0:$PORT"
