from config.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv("DB_NAME_DEV"),
    'USER': os.getenv("DB_USER_DEV"),
    'PASSWORD': os.getenv("DB_PASSWORD_DEV"),
    'HOST': os.getenv("DB_HOST_DEV"),
    'PORT': os.getenv("DB_PORT"),
}
