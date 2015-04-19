#!/bin/sh

if [ -d /media/1/cameras/camera1 ]; then
  if [ -d /media/2/cameras/camera1 ]; then
    sudo find /media/2/cameras/camera1 -type f -mmin +10 -exec mv -f {} /media/1/cameras/camera1 \;
  fi
fi
