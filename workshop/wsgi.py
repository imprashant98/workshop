"""
WSGI config for workshop project.

This file configures the WSGI (Web Server Gateway Interface) application, which serves as
the entry point for serving the Django application in production environments.

The WSGI callable is exposed as a module-level variable named ``application``.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os  # Provides functions to interact with the operating system

from django.core.wsgi import get_wsgi_application  # Default WSGI application for Django

# Set the default settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop.settings')

# Create and expose the WSGI application instance
# This will be used by WSGI servers (e.g., Gunicorn, uWSGI) to serve the project
application = get_wsgi_application()
