# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

import environ

root = environ.Path(__file__) - 2
env = environ.Env()
environ.Env.read_env()

DEBUG = env('DEBUG', default=True, cast=bool)
SITE_ID = env('SITE_ID', default='1', cast=int)

# Make these unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY')
NEVERCACHE_KEY = env('NEVERCACHE_KEY')

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

DATABASES = {
    'default': env.db('DB_URL', default='sqlite:///{0}/default.db'.format(root))
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

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
    'provider.google.api_key': env('GOOGLE_MAPS_API_KEY', default=''),
}

USE_S3 = env.bool('USE_S3', default=False)

# OIDC configuration

SITE_URL = env('SITE_URL')
OIDC_RP_CLIENT_SECRET_ENCODED = env.bool('OIDC_RP_CLIENT_SECRET_ENCODED', default=True)
AUTH0_DOMAIN = env('AUTH0_DOMAIN', default='')
AUTH0_CLIENT_ID = env('AUTH0_CLIENT_ID', default='')
OIDC_OP_AUTHORIZATION_ENDPOINT = env('OIDC_OP_AUTHORIZATION_ENDPOINT', default='')
OIDC_OP_TOKEN_ENDPOINT = env('OIDC_OP_TOKEN_ENDPOINT', default='')
OIDC_OP_USER_ENDPOINT = env('OIDC_OP_USER_ENDPOINT', default='')
OIDC_RP_CLIENT_ID = env('OIDC_RP_CLIENT_ID', default='')
OIDC_RP_CLIENT_SECRET = env('OIDC_RP_CLIENT_SECRET', default='')
OIDC_OP_DOMAIN = env('OIDC_OP_DOMAIN', default='')
