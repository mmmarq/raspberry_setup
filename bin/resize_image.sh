#!/bin/sh

CONVERT="/usr/bin/convert"
LOCK="/tmp/.resize_image.sh"

#CHECK IF LOCK FILE EXIST
if [ -f $LOCK ]; then exit 0; fi

#REMOVE LOCK FILE IN CASE SCRIPT EXIT
trap 'rm -f $LOCK' 1 2 3 9 10 11 13 15

#CREATE LOCK FILE
touch $LOCK

#MOVE TO IMAGE FOLDER
cd /media/1/share/Resize/Original

#FOR EACH IMAGE FILE
for i in `ls`
do
  #RESIZE FILE
  $CONVERT $i  -units PixelsPerInch -resample 150 -quality 100 -resize 50% /media/1/share/Resize/Final/$i
  #IF RESIZE SUCCESS
  if [ $? -eq 0 ]
  then
    #REMOVE ORIGINAL FILE
    rm -f $i
  fi
done

#REMOVE LOCK FILE
rm -f $LOCK
