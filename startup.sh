#!/usr/bin/env bash
echo "running startup..."

# Make Django migrations, just in case.
python cmstest/manage.py makemigrations

# Then migrate up, again just in case.
python cmstest/manage.py migrate

# Finally, start up the system.
python cmstest/manage.py runserver "0.0.0.0:$PORT"
