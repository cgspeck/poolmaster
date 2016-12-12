FROM python:3.5.2


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8000
EXEC python poolmaster/manage.py migrate && python poolmaster/manage.py runserver
