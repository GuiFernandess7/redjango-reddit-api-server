# settings/prod.py

from config.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv("DB_NAME_PROD"),
    'USER': os.getenv("DB_USER_PROD"),
    'PASSWORD': os.getenv("DB_PASSWORD_PROD"),
    'HOST': os.getenv("DB_HOST_prod"),
    'PORT': os.getenv("DB_PORT"),
}
