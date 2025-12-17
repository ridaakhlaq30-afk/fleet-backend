# Fleet Backend (Django API)

This backend is designed to work with the Fleet Dashboard you deployed on Vercel.

## Local run (Windows)
1) Install Python 3.11+
2) In this folder:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API runs at: http://127.0.0.1:8000

## Deploy on Render (recommended)
- Push this folder to GitHub as repo: `fleet-backend`
- Create a Render **PostgreSQL** database
- Create a Render **Web Service** from your repo
- Add environment variables (Render → Environment):
  - `SECRET_KEY` = (any long string)
  - `DEBUG` = `0`
  - `DATABASE_URL` = (auto from Render Postgres)

### Render start command
Render will run:
```
gunicorn backend.wsgi:application
```

### After first deploy
Open Render → your service → **Shell** and run:
```
python manage.py migrate
python manage.py createsuperuser
```

Then update Vercel env var `VITE_API_BASE` to your Render URL.

