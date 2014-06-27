#!/bin/sh

cat /media/2/log/`date +"%Y"`*.log | \
sed 's/\([0-9]*\)-\([0-9]*\)-\([0-9]*\) /\3,\2,\1,/g' | \
sed 's/:00 /:00,/g' | \
sed 's/ \([0-9]*$\)/,\1/g' > /media/2/log/`date +"%Y"`_local_data.csv
