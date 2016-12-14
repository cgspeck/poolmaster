#! /bin/bash
env=production

if [ ${#} -gt 1 ]; then
  cmd=${@:2}
else
  cmd=/bin/bash
fi

set -e
docker run -e ENVIRONMENT=${env} \
  --rm \
  --env-file /etc/poolmaster/poolmaster.conf \
  -v "$(pwd)/":/usr/src/app/ \
  -it \
  poolmaster \
  ${cmd}
