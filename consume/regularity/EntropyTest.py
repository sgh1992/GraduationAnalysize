#  -*- coding: utf-8 -*-

import StudentEntropy as se

startIndex = 3
termList = [1, 2, 3, 4, 5, 6, 7, 8]
type='librarydoor'
year='2010'
meal = 'dinner'
workList = ['录研', '就业', '出国深造', '其它']

#se.getEntropyData(startIndex, type, termList, workList, year, meal)
se.plotEntropy(startIndex, type, termList, workList, year, meal)

#plot Distribution
term = 1
work = 'all'
startIndex = 3
type = 'mess'
#se.plotDistribution(startIndex, type, term, work, year, meal)
# for work in workList:
#     se.plotDistribution(startIndex, type, term, work, year, meal)