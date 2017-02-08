#!/bin/sh

# REFERENCE
# http://acd-cli.readthedocs.io/en/latest/usage.html
# http://xmodulo.com/access-amazon-cloud-drive-command-line-linux.html

UPLOADER="/usr/local/bin/acd_cli -nl"
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
  echo "Motion uploader lock file found!"
  CURR_AGE=`date +%s`
  LOCK_AGE=`stat -L --format %Y $TEMP_FILE`
  AGE=`expr $CURR_AGE - $LOCK_AGE`
  if [ $AGE -lt 1800 ]; then
    echo "Motion uploader running. Do no run another task in parallel!"
    exit 0
  else
    echo "Motion uploader lock file looks like too old. Lets remove it and run again!"
    echo $$ > $TEMP_FILE
  fi
else
  echo $$ > $TEMP_FILE
fi

# REFRESH CACHE
$UPLOADER sync

# CREATE CURRENT DATA FOLDER
CURR_DATE=`date +%Y-%m-%d`
$UPLOADER mkdir --parents /Videos/Motion/$CURR_DATE

FILES=`find /mnt/media/cameras/camera1 -mmin +10`

for file in $FILES; do
  FILE_DATE=`echo $file | sed 's/-[0-9]*_.*$//g' | sed 's/^.*\///g'`
  $UPLOADER ul --force --remove-source-files --quiet $file /Videos/Motion/$FILE_DATE
done

rm -f $TEMP_FILE
