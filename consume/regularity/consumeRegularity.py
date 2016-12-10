# !/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
regularityWithWork = '/home/sghipr/consumeRegularityWithWork.csv'
def analysizeRegularity(startIndex,term,type,classValue,year='2010',meal='allMeal'):
    """
    针对不同的学生群体进行分析
    :param startIndex: 时间段的划分之始.
    :param term:学期.
    :param type: 消费类别.
    :param classValue:毕业去向群体.
    :param year: 毕业年级.
    :param meal: 早,午,晚三餐.
    :return:
    """
    data = [line.strip().decode('utf8').split(",") for line in open(regularityWithWork)]
    timeInterals = getInteralTime('allMeal')
    mealInterals = getInteralTime(meal)
    interalLists = sorted(timeInterals.keys())
    for line in data:
        studentID = line[0]
        sterm = line[1]
        stype = line[2]
        sclassValue = line[-1]
        if condition(studentID, sterm, stype, sclassValue, term, type, classValue, year):
            for index in range(startIndex,len(line)-1):
                if interalLists[index - startIndex] in mealInterals:
                    mealInterals[interalLists[index - startIndex]] += int(line[index])

    result = sorted(mealInterals.items(), key= lambda x:x[0])
    xList = []
    yList = []
    for x, y in result:
        if x > '0600' and x < '2000':
            xList.append(x)
            yList.append(y)

    sumValue = getSumValue(data,year,classValue)
    for i in range(0,len(yList)):
        yList[i] /= sumValue

    title = type + ',' + str(term) + ',' + year + ',' + classValue + ',' + meal
    plt.figure(figsize=(20,9))
    plt.plot(range(1,len(xList) + 1),yList,color='black', markersize=10)
    plt.grid(True)
    plt.xticks(range(1,len(xList) + 1),xList,rotation=45)
    plt.ylabel('frequences')
    plt.title(title)
    plt.savefig('/home/sghipr/GraduationThesis/pictures/' + title + '.png')


def getSumValue(data,year,classValue,t=180.0):
    sidSet = set()
    for line in data:
        studentID = line[0]
        sclassValue = line[-1]
        if classValue == u'allClass':
            sclassValue = classValue
        if year == u'2010':
            if studentID.startswith('2010') and sclassValue == classValue:
                sidSet.add(studentID)
        elif year == u'2009':
            if (not studentID.startswith('2010')) and sclassValue == classValue:
                sidSet.add(studentID)
    return len(sidSet) * t


def getInteralTime(meal):
    timeInterals = dict()
    if meal == 'allMeal':
        timeInterals['0000-0030'] = 0
        timeInterals['0030-0100'] = 0
        timeInterals['0100-0130'] = 0
        timeInterals['0130-0200'] = 0
        timeInterals['0200-0230'] = 0
        timeInterals['0230-0300'] = 0
        timeInterals['0300-0330'] = 0
        timeInterals['0330-0400'] = 0
        timeInterals['0400-0430'] = 0
        timeInterals['0430-0500'] = 0
        timeInterals['0500-0530'] = 0
        timeInterals['0530-0600'] = 0
        timeInterals['0600-0630'] = 0
        timeInterals['0630-0700'] = 0
        timeInterals['0700-0730'] = 0
        timeInterals['0730-0800'] = 0
        timeInterals['0800-0830'] = 0
        timeInterals['0830-0900'] = 0
        timeInterals['0900-0930'] = 0
        timeInterals['0930-1000'] = 0
        timeInterals['1000-1030'] = 0
        timeInterals['1030-1100'] = 0
        timeInterals['1100-1130'] = 0
        timeInterals['1130-1200'] = 0
        timeInterals['1200-1230'] = 0
        timeInterals['1230-1300'] = 0
        timeInterals['1300-1330'] = 0
        timeInterals['1330-1400'] = 0
        timeInterals['1400-1430'] = 0
        timeInterals['1430-1500'] = 0
        timeInterals['1500-1530'] = 0
        timeInterals['1530-1600'] = 0
        timeInterals['1600-1630'] = 0
        timeInterals['1630-1700'] = 0
        timeInterals['1700-1730'] = 0
        timeInterals['1730-1800'] = 0
        timeInterals['1800-1830'] = 0
        timeInterals['1830-1900'] = 0
        timeInterals['1900-1930'] = 0
        timeInterals['1930-2000'] = 0
        timeInterals['2000-2030'] = 0
        timeInterals['2030-2100'] = 0
        timeInterals['2100-2130'] = 0
        timeInterals['2130-2200'] = 0
        timeInterals['2200-2230'] = 0
        timeInterals['2230-2300'] = 0
        timeInterals['2300-2330'] = 0
        timeInterals['2330-0000'] = 0
    elif meal == 'breakfast':
        timeInterals['0600-0630'] = 0
        timeInterals['0630-0700'] = 0
        timeInterals['0700-0730'] = 0
        timeInterals['0730-0800'] = 0
        timeInterals['0800-0830'] = 0
        timeInterals['0830-0900'] = 0
        timeInterals['0900-0930'] = 0
    elif meal == 'lunch':
        timeInterals['1100-1130'] = 0
        timeInterals['1130-1200'] = 0
        timeInterals['1200-1230'] = 0
        timeInterals['1230-1300'] = 0
        timeInterals['1200-1330'] = 0
    elif meal == 'dinner':
        timeInterals['1630-1700'] = 0
        timeInterals['1700-1730'] = 0
        timeInterals['1730-1800'] = 0
        timeInterals['1800-1830'] = 0
        timeInterals['1830-1900'] = 0
    else:
        print meal + ' is not right format!'
    return timeInterals

def condition(studentID,sterm,stype,sclassValue,term,type,classValue,year):
    flag = False
    if year == u'2009':
        flag = studentID.startswith('2009') and studentID.startswith('29')
    elif year == u'2010':
        flag = studentID.startswith('2010')

    if classValue == u'allClass':
        sclassValue = classValue
    if term == u'allTerm':
        sterm = term

    if flag:
        if (sterm == term) and (stype == type) and (sclassValue == classValue):
            flag = True
        else:
            flag = False
    return flag