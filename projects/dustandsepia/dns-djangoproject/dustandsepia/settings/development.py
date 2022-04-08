from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DNS_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.environ["DNS_ALLOWED_HOST_1"], 
os.environ["DNS_ALLOWED_HOST_2"], os.environ["DNS_ALLOWED_HOST_3"]]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["DNS_DB_NAME"],
        'USER': os.environ["DNS_DB_USER"],
        'PASSWORD': os.environ["DNS_DB_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')