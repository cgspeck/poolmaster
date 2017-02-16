from .default import *

DEBUG = False

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
ALLOWED_HOSTS = '*'

INSTALLED_APPS += ['storages']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = environ['AWS_STORAGE_BUCKET_NAME']
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
