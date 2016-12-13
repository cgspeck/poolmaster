#! /bin/bash -e
cd poolmaster
python manage.py migrate
gunicorn -b 0.0.0.0:8000 poolmaster.wsgi
cd -
