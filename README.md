# Poolmaster

Django backed project to keep track of pool test results.

## Running it

### Running from Source

1. Customise the example local_settings.py in `/scripts/systemd/local_settings.py` and save it to `/poolmaster/local_settings.py`.

    You may want to set up your [database](https://docs.djangoproject.com/en/1.10/ref/settings/#databases) (also [read this](https://docs.djangoproject.com/en/1.10/ref/databases/)) and [static files storage backend](https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/) if running a production like environment.

1. Make a Python 3 virtualenv and use pip to install the requirements:
```
mkvirtenv poolmaster
pip install -r requirements.txt
```

1. Run migrations: `python poolmaster/manage.py migrate`

1. Then:

    1. Run the werkzeug server with `python poolmaster/manage.py runserver_plus 0.0.0.0:8000`; or

    1. Run the gunicorn server with `./scripts/run_server.sh`

### Running from Docker

To run this in docker, customise local_settings.py file and run with:

```
docker run \
  --rm \
  -v /path/to/your/local_settings.py:/usr/src/app/poolmaster/poolmaster/settings/local_settings.py \
  -p 8000:8000 \
  -it \
  cgspeck/poolmaster
```

You can find an example local_settings.py in `/scripts/systemd`.

If you want to run from source through the docker container, then run:
```
docker run \
  --rm \
  --name poolmaster-dev \
  -v /path/to/your/local_settings.py:/usr/src/app/poolmaster/poolmaster/settings/local_settings.py \
  -v "$(pwd)/":/usr/src/app/ \
  -p 8000:8000 \
  -ti \
  cgspeck/poolmaster

```

This is available as `scripts/docker_dev.sh`

## Accessing Django-Admin

Navigate to `admin/`. You will need to run `python poolmaster/manage.py createsuperuser` and follow the prompts to create your login account.

## Data Import / Export

### Export

There are two ways to export entries from the system:

1. Use the `/export.[json|csv]` endpoint
1. Log into the Admin, click on 'Observations' then 'Export'

### Import

Log into the Admin, click on 'Observations', then 'Import' and follow the prompts to upload your data file.

## Systemd

The script `/script/deploy_systemd` will copy a service file and local_settings.py to the appropriate locations in order to run the docker container on startup.

You will need to edit `/etc/poolmaster/local_settings.py` to set up your [database](https://docs.djangoproject.com/en/1.10/ref/settings/#databases) ([and read this](https://docs.djangoproject.com/en/1.10/ref/databases/)) and [static files storage backend](https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/).

## Legals

Use at your own risk.

Favicon derived from original photography by [ABZ Private School - Own work, CC BY-SA 4.0](https://commons.wikimedia.org/w/index.php?curid=46981159) and created with [Favicon Generator. For real.](https://realfavicongenerator.net/)
