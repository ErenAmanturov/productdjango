"""
ASGI config for config configject.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoconfigject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

application = get_asgi_application()
