"""
WSGI configuration file tailored for PythonAnywhere deployment of this project.

Place this file on PythonAnywhere (or point the Web app's WSGI file to it),
then edit the PROJECT_HOME and VENV_PATH variables if they differ.

This file:
 - ensures the project path is on sys.path
 - attempts to activate a virtualenv if the path exists
 - loads environment variables from a .env file (if python-dotenv is installed)
 - sets DJANGO_SETTINGS_MODULE to 'django_exam.settings'
 - exposes the WSGI `application` callable

Edit the PA_USERNAME, PROJECT_HOME, or VENV_PATH values below to match your PythonAnywhere setup.
"""

import os
import sys

# --------- Configuration (edit these as needed on PythonAnywhere) ---------
PA_USERNAME = os.environ.get('PA_USERNAME', 'saeedmb77')
# Default project directory on PythonAnywhere; change if you cloned into a different folder
PROJECT_HOME = f'/home/{PA_USERNAME}/django_exam'
# Path to your virtualenv (update to the actual path you create on PythonAnywhere)
VENV_PATH = f'/home/{PA_USERNAME}/.virtualenvs/your-venv'
# ------------------------------------------------------------------------

# Add the project directory to the PYTHONPATH
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

# Optionally activate the virtualenv by executing its activation script (if present)
if os.path.exists(VENV_PATH):
    activate_script = os.path.join(VENV_PATH, 'bin', 'activate_this.py')
    if os.path.exists(activate_script):
        try:
            with open(activate_script) as f:
                exec(f.read(), {'__file__': activate_script})
        except Exception:
            # Activation via activate_this.py failed; the Web tab virtualenv setting usually suffices
            pass

# Try loading environment variables from a .env file in the project root (optional)
try:
    from dotenv import load_dotenv

    dotenv_path = os.path.join(PROJECT_HOME, '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
except Exception:
    # python-dotenv might not be installed in the system virtualenv yet
    pass

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_exam.settings')

# Finally import Django and get the WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
