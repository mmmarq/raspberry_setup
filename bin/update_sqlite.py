#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
from time import localtime, strftime



con = sqlite3.connect('/media/2/code/test/test.db')
#Log data on database
date = strftime("%Y-%m-%d %H:%M", localtime())
mySql = 'INSERT INTO weather_data VALUES("' + date + '",' + '111' + ',' + '222' + ')'
with con:
   cur = con.cursor()
   cur.execute(mySql)

