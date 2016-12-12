#! /bin/bash -e
export ENVIRONMENT=production
cd poolmaster
python manage.py migrate
gunicorn poolmaster.wsgi
cd -
