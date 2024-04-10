from storefront.settings.common import *
import dj_database_url
import os


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:storeback-ocean.flycast:5432",
        conn_max_age=600,
    )
}

ALLOWED_HOSTS = ['storeback-ocean.fly.dev']
CSRF_TRUSTED_ORIGINS = ['https://storeback-ocean.fly.dev']
