from django.apps import AppConfig  # Import base configuration class for Django apps

# Define configuration for the 'book' app
class BookConfig(AppConfig):
    # Specifies the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specifies the name of the app as it appears in the project
    name = 'book'
