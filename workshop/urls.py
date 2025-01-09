"""
URL configuration for the workshop project.

The `urlpatterns` list is used to route URLs to their corresponding views. For more information, visit:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  # Admin site functionality
from django.urls import path, include  # Utilities for defining URL routes and including other URL configs
from django.conf import settings  # Access project settings
from django.conf.urls.static import static  # Utility for serving static/media files in development

# Swagger schema view setup
from drf_yasg import openapi  # OpenAPI schema generation utilities
from drf_yasg.views import get_schema_view  # View for rendering the API documentation
from rest_framework import permissions  # Permission utilities from Django REST Framework

# Schema view for API documentation using Swagger and ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="Workshop Demo API",  # Title of the API documentation
        default_version='v1',  # Version of the API
        description="API documentation for workshop project",  # Brief description of the API
        terms_of_service="https://swagger.io/resources/open-api/",  # Terms of service URL
        contact=openapi.Contact(email="prashantkarna21@gmail.com"),  # Contact information
        license=openapi.License(name="MIT License"),  # License for the API
    ),
    public=True,  # Make the schema publicly available
    permission_classes=(permissions.AllowAny,),  # Allow access to the schema for all users
)

# URL patterns define how requests to specific URLs are routed to views
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),  # URL for Django's admin interface

    # API endpoints for the 'book' app
    path('api/', include('book.urls')),  # Includes URLs from the `book` app

    # API documentation views
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI for interactive API docs
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI for API docs
]

# In development mode, serve static and media files through Django
if settings.DEBUG:
    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
