from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# pip install psycopg2
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),  # Or the appropriate host name
        'PORT': os.environ.get('DATABASE_PORT'),       # Or the appropriate port
    }
}


# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')


# Media files (user uploaded files)
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../mediafiles')