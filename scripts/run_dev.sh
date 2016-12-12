#! /bin/bash -e
cd poolmaster
python manage.py migrate
python manage.py runserver_plus
cd -
