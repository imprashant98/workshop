#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Shebang line specifies that this script should be executed using the Python interpreter 
# found in the current environment. This ensures portability.

import os  # Module to interact with the operating system (e.g., setting environment variables)
import sys  # Module to interact with command-line arguments and system-specific functions


def main():
    """Run administrative tasks."""
    # Set the default environment variable for Django settings module.
    # This points Django to the correct settings file ('workshop.settings' in this case).
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop.settings')
    
    try:
        # Import Django's management command-line utility to execute commands (e.g., runserver, migrate)
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle the case where Django is not installed or not accessible.
        # Raise an error with a clear message about missing Django or incorrect PYTHONPATH.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command-line arguments passed to this script.
    # For example, `python manage.py runserver` will run the Django development server.
    execute_from_command_line(sys.argv)


# The entry point of the script.
# This ensures the `main()` function is executed only if the script is run directly,
# not when imported as a module.
if __name__ == '__main__':
    main()
