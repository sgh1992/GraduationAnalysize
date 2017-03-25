# !/usr/bin/python
#  -*- coding: utf-8 -*-
import ConsumeRegularity as regu

startIndex = 3
term = u'1'
type = u'mess'
year = u'2010'
classValue = u'出国出境'
meal = 'dinner'
termList = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8']
classValueList = [u'就业',u'录研',u'出国深造',u'其它']
mealList = ['breakfast', 'lunch', 'dinner','allMeal']
# regu.analysizeRegularity(startIndex,term,type,classValue,year,meal)

# for classValue in classValueList:
#     regu.analysizeRegularity(startIndex,term,type,classValue,year)

# for classValue in classValueList:
#     for term in termList:
#         for meal in mealList:
#             regu.analysizeRegularity(startIndex,term,type,classValue,year,meal)
# regu.analysizeTotalRegularity(startIndex,term,type,classValueList,year,meal)


# for term in termList:
#     xLists,yLists = regu.analysizeTotalRegularity(startIndex,term,type,classValueList,year,meal)
#     title = type.encode('utf-8') + '_term' + term.encode('utf-8')
#     regu.plotMultiplePictures(xLists,yLists,classValueList,title)

regu.plotTermAxPictures(startIndex, type, classValueList, year, meal)
# mealList = ['breakfast', 'lunch', 'dinner']
# for meal in mealList:
#     regu.plotTermAxPictures(startIndex, type, classValueList, year, meal)

#regu.analysizeTermDistance(startIndex, type, classValueList, year, meal)









