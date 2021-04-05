from decouple import config

from {{ project_name }}.settings import constants
from {{ project_name }}.settings.base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DATABASE_NAME', default='{{ project_name }}_hml'),
        'USER': config('MYSQL_USER', default='root'),
        'PASSWORD': config('MYSQL_PASSWORD', default='root'),
        'HOST': config('MYSQL_HOST', default='127.0.0.1'),
        'PORT': config('MYSQL_PORT', default='3306'),
        'CONN_MAX_AGE': 4 * constants.HOURS,
    }
}
