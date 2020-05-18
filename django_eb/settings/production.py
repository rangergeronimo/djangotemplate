from .base import *

# Configure remote domain name
ALLOWED_HOSTS = [os.environ['WEBSITE_DOMAIN'] if 'WEBSITE_DOMAIN' in os.environ else []]

DEBUG = False

# installed apps 
INSTALLED_APPS += []

# Remote Postgres Database Setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_DB_NAME'],
        'PASSWORD': os.environ['RDS_DB_NAME'],
        'HOST': os.environ['RDS_DB_NAME'],
        'PORT': int(os.environ['RDS_DB_PORT'])
    }
}

# static files setup 
STATIC_URL = "/static/"

STATIC_ROOT = (BASE_DIR, 'static')

