#!/bin/sh

DISK=`df | grep /media/1`

if [ "x$DISK" = "x" ]
then
  echo "Mounting remote disk /media/1"
  mount /media/1
  echo "Restarting services"
  /etc/init.d/transmission-daemon restart
  /etc/init.d/btsync restart
  echo "Done"
fi

