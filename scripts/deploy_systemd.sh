#! /bin/bash -e
if [ ! -f /etc/poolmaster/poolmaster.conf ]; then
  mkdir /etc/poolmaster
  cp scripts/systemd/poolmaster.conf /etc/poolmaster/
fi
cp scripts/systemd/poolmaster.service /etc/systemd/system/
systemctl daemon-reload
systemctl start poolmaster.service
systemctl enable poolmaster.service
