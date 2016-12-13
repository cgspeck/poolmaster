#! /bin/bash -e
cd poolmaster
python manage.py migrate
python manage.py runserver_plus 0.0.0.0:8000
cd -
