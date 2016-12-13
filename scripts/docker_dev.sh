#! /bin/bash
set -e
docker run -e ENVIRONMENT=dev \
  --rm \
  --name poolmaster-dev \
  -v "$(pwd)/":/usr/src/app/ \
  -p 8000:8000 \
  -ti \
  poolmaster \
  /usr/src/app/scripts/run_dev.sh
