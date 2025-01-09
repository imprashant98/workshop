"""
ASGI config for workshop project.

This file configures the ASGI application, which allows Django to handle asynchronous
requests, such as WebSockets or long-lived HTTP connections.

The ASGI callable is exposed as a module-level variable named ``application``.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/


ASGI stands for Asynchronous Server Gateway Interface.


"""

import os  # Used for setting and reading environment variables

from django.core.asgi import get_asgi_application  # Default Django ASGI application handler

# Set the default Django settings module for the ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop.settings')

# Create the ASGI application instance that will be used to serve requests
application = get_asgi_application()


# Alternatively we can use WSGI too instead of ASGI but it's more common to use ASGI because it's more efficient and 
# supports both HTTP and WebSocket, ideal for real-time bidirectional communication