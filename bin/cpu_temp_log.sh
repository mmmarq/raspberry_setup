#!/bin/sh

#DATE=`date +%Y-%m-%d`
DATE=`date "+%Y-%m-%d %H:%M"`
TEMP=`/opt/vc/bin/vcgencmd measure_temp`

echo "$DATE - $TEMP"

