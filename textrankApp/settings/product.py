import os

from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

# 운영 모드는 debug false
DEBUG = False

# AWS Example
ALLOWED_HOSTS = ['jkhyjkhy.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
