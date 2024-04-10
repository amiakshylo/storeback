from storefront.settings.common import *
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False



DATABASES = {
    "default": dj_database_url.config(
        default="postgres://mysite:YAQatcmxundCJm9clHOqE7UqoyqUHwN4@dpg-cncfupeg1b2c739hm6l0-a/mysite_8gpf",
        conn_max_age=600,
    )
}

APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]