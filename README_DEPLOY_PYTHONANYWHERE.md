Deployment steps for PythonAnywhere

1) Create a PythonAnywhere account and open a Bash console.

2) Clone your repository (you already did this):
   git clone https://github.com/<your-username>/<your-repo>.git

3) Create and activate a virtualenv (use Python 3.11/3.12 if available):
   python3 -m venv ~/venv/<your-username>-django
   source ~/venv/<your-username>-django/bin/activate

4) Install dependencies:
   pip install -r requirements.txt

5) Copy the example env and set values:
   cp .env.example .env
   # then edit .env and set DJANGO_SECRET_KEY and DJANGO_ALLOWED_HOSTS

6) Collect static files:
   python manage.py collectstatic --noinput

7) Create the database (if not using existing sqlite):
   python manage.py migrate

8) In the PythonAnywhere Web tab:
   - Set the source path to your project directory
   - Set the WSGI configuration file to point to django_exam.wsgi
   - Configure virtualenv path to the virtualenv you created

9) Environment variables:
   - On PythonAnywhere, add the env vars from `.env` into the "Environment Variables" section (or rely on .env in your repo if you prefer).

10) Reload the web app from the Web tab.

WSGI helper file

If you prefer to use a custom WSGI file bundled with the repository, point the "WSGI configuration file" field in the PythonAnywhere Web tab to:

    /home/<your-username>/django_exam/pythonanywhere_wsgi.py

Edit the top of that file to set `PA_USERNAME`, `PROJECT_HOME` and `VENV_PATH` to your values (the defaults assume you cloned into `~/django_exam`).

Environment variables

You can either paste the variables from `.env` into the Web tab's Environment Variables section, or rely on the `.env` file with `python-dotenv` (the bundled `pythonanywhere_wsgi.py` will attempt to load it if present).

Notes:
- Ensure `STATIC_ROOT` in settings.py is set (this project uses `staticfiles/`) and that you ran `collectstatic`.
- If you use sqlite, upload `db.sqlite3` to the home directory or create a new DB via migrations.
- For API access from a mobile app, point to https://<your-username>.pythonanywhere.com/api/deliveries/ (ensure CORS if needed).
- Keep DEBUG=False in production and set a strong SECRET_KEY.
