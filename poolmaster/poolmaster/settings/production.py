from os import environ

from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ['DB_NAME'],
        'USER': environ['DB_USER'],
        'PASSWORD': environ['DB_PASSWORD'],
        'HOST': environ['DB_HOST'],
        'PORT': environ['DB_PORT'],
    }
}
SECRET_KEY = environ['SECRET_KEY']
ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split(',')
