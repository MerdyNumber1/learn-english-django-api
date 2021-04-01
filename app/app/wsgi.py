"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# sys.path.insert(0, os.path.join(os.getcwd(), 'app'))
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'app.app.settings'
# os.environ['ROOT_URLCONF'] = 'app.app.urls'
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

application = get_wsgi_application()

