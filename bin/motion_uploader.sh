#!/bin/sh

UPLOADER="/mnt/code/motion-uploader/uploader.py"
TEMP_FILE="/tmp/motion_uploader.tmp"

trap cleanup 1 2 3 6 9 15

cleanup()
{
  echo "Caught Signal ... cleaning up."
  rm -f $TEMP_FILE
  echo "Done cleanup ... quitting."
  exit 1
}


if [ -f $TEMP_FILE ]; then
  echo "Motion uploader running. Do no run another task in parallel"
  exit 0
else
  echo $$ > $TEMP_FILE
fi

FILES=`find /mnt/media/cameras/camera1 -mmin +10`

for file in $FILES; do
  $UPLOADER /home/pi/uploader.cfg $file
done

rm -f $TEMP_FILE

