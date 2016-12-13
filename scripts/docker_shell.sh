#! /bin/bash
set -e
docker run -e ENVIRONMENT=dev \
  --rm \
  --name poolmaster-dev \
  -v "$(pwd)/":/usr/src/app/ \
  -ti \
  poolmaster \
  python /usr/src/app/poolmaster/manage.py shell_plus
