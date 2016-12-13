#! /bin/bash -e
mkdir /etc/poolmaster
if [ ! -f /etc/poolmaster/poolmaster.conf ]; then
  cp scripts/systemd/poolmaster.conf /etc/poolmaster/
fi
cp scripts/systemd/poolmaster.unit /etc/systemd/system/
systemctl daemon-reload
systemctl start poolmaster.service
systemctl enable poolmaster.service
