from .common import *
import os
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['storefront-epcj.onrender.com']

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://storefront_t6c8_user:yBxTinAcfwv7WoyKQbNakyQyBtv4USBI@dpg-cncfemen7f5s73bgb8dg-a/storefront_t6c8',
        conn_max_age=600
    )
}