import os
import sys

def start_system():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblio_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django non trouvé. Verifiez l'activation du venv."
        ) from exc
    
    execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000'])

if __name__ == '__main__':
    start_system()