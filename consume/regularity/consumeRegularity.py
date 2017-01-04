# !/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import pandas as pd

regularityWithWork = 'D:/GraduationThesis/librarydoor_regularityWithWork_TimeSelf.csv'
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
    timeInterals = getInteralTime('librarydoor')
    mealInterals = getInteralTime(meal)
    interalLists = sorted(timeInterals.keys())
    for line in data:
        studentID = line[0]
        sterm = line[1]
        stype = line[2]
        sclassValue = line[-1]
        if condition(studentID, sterm, stype, sclassValue, term, type, classValue, year):
            for index in range(startIndex, len(line)-1):
                if interalLists[index - startIndex] in mealInterals:
                    mealInterals[interalLists[index - startIndex]] += int(line[index])

    result = sorted(mealInterals.items(), key=lambda x:x[0])
    xList = []
    yList = []
    for x, y in result:
        #if x > '0600' and x < '2000':
        xList.append(x)
        yList.append(y)

    sumValue = getSumValue(data,year,classValue)
    for i in range(0,len(yList)):
        yList[i] /= sumValue
    title = type + ',' + str(term) + ',' + year + ',' + classValue + ',' + meal
    return xList,yList,title


def analysizeTermDistance(startIndex, type, classValueList, year='2010', meal='allMeal'):
    """
    横向与纵向对比不同群体的学生之间的差异性与不同学期之间的变化幅度的差异性.
    横向：同一学期之间不同群体的对比
    纵向：不同学期同一群体之间的对比
    """
    classValueDict = {}
    for term in range(1, 9):
        uterm = str(term).decode('utf-8')
        for classValue in classValueList:
            xList,yList,title = analysizeRegularity(startIndex, uterm, type, classValue, year, meal)
            classValueDict.setdefault(classValue.encode('utf-8'), [])
            classValueDict[classValue.encode('utf-8')].append(sum(yList))

    classValuePd = DataFrame(classValueDict,index=['term1', 'term2', 'term3', 'term4', 'term5', 'term6', 'term7', 'term8'])
    classValuePd['比就业'] = (classValuePd['就业']-classValuePd['录研'])/classValuePd['录研']
    classValuePd['比出国深造'] = (classValuePd['出国深造']-classValuePd['录研'])/classValuePd['录研']
    classValuePd['比其它'] = (classValuePd['其它']-classValuePd['录研'])/classValuePd['录研']

    classValuePd.loc['CTerm2'] = (classValuePd.ix['term2'] - classValuePd.ix['term1'])/classValuePd.ix['term1']
    classValuePd.loc['CTerm3'] = (classValuePd.ix['term3'] - classValuePd.ix['term1'])/classValuePd.ix['term1']
    classValuePd.loc['CTerm4'] = (classValuePd.ix['term4'] - classValuePd.ix['term1'])/classValuePd.ix['term1']
    classValuePd.loc['CTerm5'] = (classValuePd.ix['term5'] - classValuePd.ix['term1'])/classValuePd.ix['term1']
    classValuePd.loc['CTerm6'] = (classValuePd.ix['term6'] - classValuePd.ix['term1'])/classValuePd.ix['term1']
    classValuePd.loc['CTerm7'] = (classValuePd.ix['term7'] - classValuePd.ix['term1'])/classValuePd.ix['term1']
    classValuePd.loc['CTerm8'] = (classValuePd.ix['term8'] - classValuePd.ix['term1']) / classValuePd.ix['term1']

    print classValuePd

    result = 'D:/GraduationThesis/Data/' + meal.encode('utf-8') + 'DataCompare3.csv'
    classValuePd.to_csv(result)

def analysizeTotalRegularity(startIndex,term,type,classValueList,year='2010',meal='allMeal'):
    xLists = []
    yLists = []
    labelList = []
    for classValue in classValueList:
        xList, yList, title = analysizeRegularity(startIndex, term, type, classValue, year, meal)
        xLists.append(xList)
        yLists.append(yList)
        labelList.append(classValue)

    # title = term + ',' + type + ','
    # for classValue in classValueList:
    #     title = title + '-' + classValue

    return xLists,yLists

    #plotMultiplePictures(xLists, yLists, labelList,title)


def plotMultiplePictures(xLists, yLists, labelList, title):
    """
    将多个不同毕业去向的群体的学生的行为表达在一个图中.
    """
    plt.figure(figsize=(21, 9))
    for xList, yList, label in zip(xLists, yLists, labelList):
        plt.plot(range(1, len(xList) + 1), yList, markersize=10, label=label)
        plt.grid(True)

    plt.xticks(range(1, len(xLists[0]) + 1), xList, rotation=45)
    plt.ylabel('frequences')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    result = 'D:/GraduationThesis/pictures/' + title + '.pdf'
    plt.savefig(result)


def plotTermAxPictures(startIndex, type, classValueList, year='2010', meal='allMeal'):

    """
    针对type在六个学期的变化情况.(例如type取早餐)
    默认是六个学期.
    因此整个图形就是3行2列的布局.
    """
    fig, axes = plt.subplots(4, 2, sharex=True, sharey=True, figsize=(12, 8))

    plotAxPictures(axes[0,0], u'1', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[0,1], u'2', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[1,0], u'3', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[1,1], u'4', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[2,0], u'5', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[2,1], u'6', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[3,0], u'7', startIndex, type, classValueList, year, meal)
    plotAxPictures(axes[3,1], u'8', startIndex, type, classValueList, year, meal)

    fig.tight_layout()

    result = 'D:/GraduationThesis/pictures/' + meal.encode('utf-8') + 'AllCompare8.pdf'
    fig.savefig(result)



def plotAxPictures(ax,term,startIndex,type, classValueList,year,meal):
    """
    一个大图中的子图.
    """
    plt.sca(ax)
    xLists,yLists = analysizeTotalRegularity(startIndex,term,type,classValueList,year,meal)

    for xList, yList, label in zip(xLists, yLists, classValueList):
        plt.plot(range(1, len(xList) + 1), yList, label=label)
        plt.grid(True)

    plt.xticks(range(1, len(xLists[0]) + 1), xList, rotation=45)#rotation=45
    plt.title('term' + str(term))
    plt.legend(loc='best', fontsize = 'x-small')
    plt.tight_layout()
    # result = 'D:/GraduationThesis/pictures/' + meal.encode('utf-8') + '_term' + term.encode('utf-8')+'AllCompare8.pdf'
    # plt.savefig(result)





def plotPictures(title,xList,yList):

    plt.figure(figsize=(20,9))
    plt.plot(range(1,len(xList) + 1),yList,color='black', markersize=10)
    plt.grid(True)
    plt.xticks(range(1,len(xList) + 1),xList,rotation=90)
    plt.ylabel('frequences')
    plt.title(title)
    plt.tight_layout()
    plt.savefig('D:/GraduationThesis/pictures/' + title + '.pdf')



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

def getWeekInteralTime():
    timeInterals = dict()
    timeInterals['Monday'] = 0
    timeInterals['Tuesday'] = 0
    timeInterals['Wednesday'] = 0
    timeInterals['Thursday'] = 0
    timeInterals['Friday'] = 0
    timeInterals['Saturday'] = 0
    timeInterals['Sunday'] = 0
    return timeInterals


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
        timeInterals['1030-1100'] = 0
        timeInterals['1100-1130'] = 0
        timeInterals['1130-1200'] = 0
        timeInterals['1200-1230'] = 0
        timeInterals['1230-1300'] = 0
        timeInterals['1300-1330'] = 0
    elif meal == 'dinner':
        timeInterals['1630-1700'] = 0
        timeInterals['1700-1730'] = 0
        timeInterals['1730-1800'] = 0
        timeInterals['1800-1830'] = 0
        timeInterals['1830-1900'] = 0
    elif meal == 'librarydoor':
        timeInterals['0700-0830'] = 0
        timeInterals['0830-1005'] = 0
        timeInterals['1005-1200'] = 0
        timeInterals['1200-1430'] = 0
        timeInterals['1430-1605'] = 0
        timeInterals['1605-1800'] = 0
        timeInterals['1800-1930'] = 0
        timeInterals['1930-2030'] = 0
        timeInterals['2030-2200'] = 0
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