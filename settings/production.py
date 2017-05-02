import os
from django.conf import settings


DEBUG = False
TEMPLATE_DEBUB = True

DATABASES = settings.DATABASES

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

# SATICFILES_DIRS = (
# 	os.path.join(BASE_DIR, 'static'),
# 	)