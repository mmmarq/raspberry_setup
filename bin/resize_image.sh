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
if [ ! -d /media/1/share/Resize/Original ]; then
  #REMOVE LOCK FILE
  rm -f $LOCK
  exit 0
fi

cd /media/1/share/Resize/Original

if  [ ! -d /media/1/share/Resize/Final ]; then
  mkdir -p /media/1/share/Resize/Final
fi

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
