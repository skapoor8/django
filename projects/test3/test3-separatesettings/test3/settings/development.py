from test3.settings.base import *
import os



SECRET_KEY = os.environ["TEST3_SECRET_KEY"]


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ["TEST3_ALLOWED_HOST_1"]]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["TEST3_DB_NAME"],
        'USER': os.environ["TEST3_DB_USER"],
        'PASSWORD': os.environ["TEST3_DB_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')