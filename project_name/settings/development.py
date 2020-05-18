from .base import *

# Configure remote domain name
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

DEBUG = True

# installed apps 
INSTALLED_APPS += []


#Database Setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': int(os.environ['DB_PORT'])
    }
}

# static files setup 
STATIC_URL = "/static/"

STATICFILES_DIRS = [ BASE_DIR, 'staticfiles']
