from config.settings.base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB_DEV"),
        'TEST': {
            'NAME': os.getenv("POSTGRES_DB_DEV"),
        },
        'USER': os.getenv("POSTGRES_USER_DEV"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD_DEV"),
        'HOST': 'db',
        'PORT': '5432',
    }
}