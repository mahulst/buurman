from __future__ import absolute_import, unicode_literals

from .base import *
from .secret import *
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/data/buurman/db.sqlite3')
    }
}

MEDIA_ROOT = os.path.join('/data/buurman/media')

try:
    from .local import *
except ImportError:
    pass
