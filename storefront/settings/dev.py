from .common import *

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'storedb',
        'HOST': 'postgres',
        'USER': 'root',
        'PASSWORD': 'mypassword',
        'PORT': '5432',

    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'localstorebackdb',
#         'HOST': 'localhost',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'PORT': '5432',
#
#     }
# }

CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORDS = ''
EMAIL_PORT = 2525

# if DEBUG:
#     MIDDLEWARE += ['silk.middleware.SilkyMiddleware']


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'http://192.168.22.2/']
