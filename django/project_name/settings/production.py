from decouple import config

from {{ project_name }}.settings.base import *  # noqa

DEBUG = False

# Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME', default='{{ project_name }}'),
        'USER': config('DATABASE_USER', default='{{ project_name }}'),
        'PASSWORD': config('DATABASE_PASSWORD', default='{{ project_name }}'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default='5432', cast=int),
    }
}

# Logging
LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': 'app.log',
    'maxBytes': 1024 * 1024 * 3,  # 5 MB
    'backupCount': 1,
    'formatter': 'verbose',
}

LOGGING['loggers']['django.request']['handlers'] = ['file']
LOGGING['loggers']['']['handlers'] = ['file']
LOGGING['loggers']['']['level'] = 'DEBUG'
LOGGING['loggers']['django.db.backends'] = {
    'handlers': ['null'],  # Quiet by default!
    'propagate': False,
    'level': 'INFO',
}