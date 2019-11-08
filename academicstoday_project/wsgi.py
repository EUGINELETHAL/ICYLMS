"""
WSGI config for academicstoday_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from manage import DEFAULT_SETTINGS_MODULE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "academicstoday_project.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

