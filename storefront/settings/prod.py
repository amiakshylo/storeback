from storefront.settings.common import *
import dj_database_url
import os


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:iVHzXGtX4tkUlXj@storeback-db.flycast:5432",
        conn_max_age=600,
    )
}

ALLOWED_HOSTS = ['storeback.fly.dev']
CSRF_TRUSTED_ORIGINS = ['https://storeback.fly.dev']
