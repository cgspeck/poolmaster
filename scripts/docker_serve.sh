#! /bin/bash
set -e
docker run \
  --env-file /etc/poolmaster/poolmaster.conf \
  --rm \
  --name poolmaster \
  -p 8000:8000 \
  poolmaster
