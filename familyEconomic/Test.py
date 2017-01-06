# !/usr/bin/python
#  -*- coding: utf-8 -*-

import Estimate as Es

file = '/home/sghipr/consumeMess.csv_addWork.csv'
startIndex = 2
year = '2010'
workList = ['就业','录研', '出国深造', '其它']
type = 'messRate'
Es.plotSituation(file,startIndex,workList,year,type)