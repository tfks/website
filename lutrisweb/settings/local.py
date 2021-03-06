import os
from lutrisweb.settings.base import *  # noqa

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

if os.environ.get('USE_SQLITE') != "1":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'lutris',
            'USER': 'lutris',
            'PASSWORD': 'admin',
            'HOST': os.environ.get("DB_HOST", "localhost"),
        }
    }
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/lutris-emails'

STEAM_API_KEY = os.environ.get('STEAM_API_KEY')
