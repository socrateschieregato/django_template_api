from decouple import config

from {{ project_name }}.settings import constants
from {{ project_name }}.settings.base import *  # noqa

# MySql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DATABASE_NAME', default='{{ project_name }}_dev'),
#         'USER': config('DATABASE_USER', default='root'),
#         'PASSWORD': config('DATABASE_PASSWORD', default='root'),
#         'HOST': config('DATABASE_HOST', default='127.0.0.1'),
#         'PORT': config('DATABASE_PORT', default='3306'),
#         'CONN_MAX_AGE': 4 * constants.HOURS,
#     }
# }

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