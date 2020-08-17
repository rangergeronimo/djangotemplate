from .base import *

# Configure remote domain name
ALLOWED_HOSTS = [os.environ['WEBSITE_DOMAIN'] if 'WEBSITE_DOMAIN' in os.environ else []]

DEBUG = True

# installed apps 
INSTALLED_APPS += []

# Remote Postgres Database Setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_DB_USER'],
        'PASSWORD': os.environ['RDS_DB_PASSWORD'],
        'HOST': os.environ['RDS_DB_HOST'],
        'PORT': int(os.environ['RDS_DB_PORT'])
    }
}

# static files setup 
STATIC_URL = "/static/"

STATIC_ROOT = (BASE_DIR, 'static')

