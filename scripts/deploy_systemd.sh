#! /bin/bash -e
if [ ! -f /etc/poolmaster/local_settings.py ]; then
  mkdir /etc/poolmaster
  cp scripts/systemd/local_settings.py /etc/poolmaster/
fi
cp scripts/systemd/poolmaster.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable poolmaster.service
