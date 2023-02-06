#! /usr/bin/env python 
import os 
import sys 

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sgnlp_finance.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Check if we can import django first, before concluding if importing is the error 
        try: 
            import django 
        except ImportError as esc:
            raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from esc 
        raise
    execute_from_command_line(sys.argv) 