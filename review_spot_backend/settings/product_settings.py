"""
Django settings for review_spot_backend project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from .base_settings import *
from corsheaders.defaults import default_headers, default_methods


DEBUG = False

ALLOWED_HOSTS = [
    '3.39.234.40',
    '34.123.47.125',
    '127.0.0.1',
    'localhost',
    'https://review-spot.vercel.app/',
    'http://localhost:3000',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'

# CORS 설정
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    'http://3.39.234.40',
    'http://34.123.47.125',
    'http://127.0.0.1',
    'http://localhost',
    'https://review-spot.vercel.app',
    'http://localhost:3000',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'review_spot_main',
        'USER': 'developer',
        'PASSWORD': 'reviewspot',
        'HOST': 'postgresql-db',
        'PORT': '5432',
    }
}

CORS_ALLOW_METHODS = list(default_methods)

CORS_ALLOW_HEADERS = list(default_headers)

sentry_sdk.init(
    dsn="https://e41547dd9fff77e3a196f283fa052b01@o4508335294119936.ingest.us.sentry.io/4508335295234048",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    _experiments={
        # Set continuous_profiling_auto_start to True
        # to automatically start the profiler on when
        # possible.
        "continuous_profiling_auto_start": True,
    },
    environment='production',
)
