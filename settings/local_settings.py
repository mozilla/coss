# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

import os
import dj_database_url

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True
SITE_ID = os.getenv('SITE_ID', '1')

# Make these unique, and don't share it with anybody.
SECRET_KEY = os.getenv("SECRET_KEY", "supposedly there was no secret_key in the env so check this out this is now a key")
NEVERCACHE_KEY = os.getenv("NEVERCACHEKEY", "yeah this nevercache_key value wasn't set so no biggie just use this string")

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

DATABASE_URL = os.getenv('DATABASE_URL', False)

if DATABASE_URL is not False:
    DATABASES['default'].update(dj_database_url.config())

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","localhost,127.0.0.1").split(",")

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }


LOCATION_FIELD = {
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': 'AIzaSyCPOOltnRybC8TimX-9Uj1DmSK7RTdHGDc',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',
}

USE_S3=False