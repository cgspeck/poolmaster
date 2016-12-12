#! /bin/bash -e
cd poolmaster
python manage.py migrate
gunicorn poolmaster.wsgi
cd -
