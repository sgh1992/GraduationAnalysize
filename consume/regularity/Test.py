# !/usr/bin/python
#  -*- coding: utf-8 -*-
import consumeRegularity as regu

startIndex = 3
term = u'1'
type = u'mess'
year = u'2010'
classValue = u'出国出境'
meal = 'allMeal'
termList = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8']
classValueList = [u'就业',u'录研',u'出国出境',u'其它']
mealList = ['breakfast', 'lunch', 'dinner','allMeal']
regu.analysizeRegularity(startIndex,term,type,classValue,year,meal)

# for classValue in classValueList:
#     regu.analysizeRegularity(startIndex,term,type,classValue,year)

# for classValue in classValueList:
#     for term in termList:
#         for meal in mealList:
#             regu.analysizeRegularity(startIndex,term,type,classValue,year,meal)
