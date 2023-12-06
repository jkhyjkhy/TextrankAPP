from .base import *

SECRET_KEY = "django-insecure-dz*khep9b_5@d7+qmwjb^&u*w86c&gs&_piy7$om!6t3_qrl)3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
