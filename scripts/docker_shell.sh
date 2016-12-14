#! /bin/bash
if [ ${#} -eq 1 ]; then
  env=$1
else
  env=dev
fi

if [ ${#} -gt 1 ]; then
  cmd=${@:2}
else
  cmd=/bin/bash
fi

set -e
docker run -e ENVIRONMENT=${env} \
  --rm \
  -v "$(pwd)/":/usr/src/app/ \
  -it \
  poolmaster \
  ${cmd}
