from .common import *
import os
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['storefront-epcj.onrender.com']

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://mysite:YAQatcmxundCJm9clHOqE7UqoyqUHwN4@dpg-cncfupeg1b2c739hm6l0-a/mysite_8gpf',
        conn_max_age=600
    )
}