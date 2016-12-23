# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
import ConsumeRegularity as conRegu
import numpy as np

"""
计算学生的行为熵
包括学生食堂一日三餐的熵和宿舍洗澡消费时的熵等.
"""

dataFile = 'D:/GraduationThesis/consumeRegularityWithWork.csv'



def figureEntropy(startIndex, type, termList, workList, year='2010', meal='breakfast'):
    """
    根据所给定的参数来计算其不同类群体学生的熵.
    meal在只有在计算type=mess时才有效.
    """
    data = [line.strip().decode('utf-8').split(',') for line in open(dataFile)]
    allTimeList = sorted(conRegu.getInteralTime('allMeal').keys())
    realTimeList = []
    if type != 'mess':
        realTimeList = allTimeList[:]

    else:
        realTimeList = sorted(conRegu.getInteralTime(meal).keys())

    entropyDict = {}
    peopleNumDict = {}

    workNums = getWorkDict(data,year,workList)
    for item in workNums.items():
        print item[0].decode('utf-8'),item[1]

    for line in data:
        studentID = line[0].encode('utf-8')
        work = line[-1].encode('utf-8')
        sterm = int(line[1])
        stype = line[2].encode('utf-8')
        if condition(studentID, stype, sterm, type, termList, year, work, workList):

            entropyDict.setdefault(work,{})
            entropyDict[work].setdefault(sterm, 0.0)

            peopleNumDict.setdefault(work, {})
            peopleNumDict[work].setdefault(sterm, set())

            peopleNumDict[work][sterm].add(studentID)
            entropyDict[work][sterm] += entropy(startIndex, line, allTimeList, realTimeList)

    for work in peopleNumDict.keys():
        for term in termList:
            entropyDict[work][term] /= len(peopleNumDict[work][sterm])

    if type == 'mess':
        return meal, entropyDict
    else:
        return type, entropyDict


def plotEntropy(startIndex, type, termList, workList, year, meal):
    """
    刻画出某个类型type的学生行为熵
    每个学期一个点，总共有八个学期；四类学生群体，共四条线.
    """
    stype, entropyDict = figureEntropy(startIndex, type, termList, workList, year, meal)
    plt.figure(figsize=(6, 4))

    for work in entropyDict.keys():
        termDict = entropyDict[work]
        itemsList = sorted(termDict.items(), key=lambda x: x[0])
        xList = []
        yList = []
        for item in itemsList:
            xList.append(item[0])
            yList.append(item[1])
        plt.plot(range(1, len(xList) + 1), yList, label=work.decode('utf-8'))
    plt.grid(True)
    plt.xticks(range(1, len(xList) + 1), xList)
    plt.xlabel('terms')
    plt.ylabel('entropy')
    plt.title(stype)
    plt.legend(loc='best')

    result = 'D:/GraduationThesis/pictures/' + stype + '_entropy.pdf'
    plt.savefig(result)


def entropy(startIndex, line, allTimeList, realTimeList):
    """
    计算每个学期的熵.
    """
    valueList = []
    for i in range(startIndex, len(line) - 1):
        time = allTimeList[i - startIndex]
        if time in realTimeList:
            valueList.append(int(line[i]))

    entropyValue = 0.0
    for value in valueList:
        if value == 0:
            continue
        probs = (value + 0.0)/sum(valueList)
        entropyValue -= (probs) * np.log(probs)
    return entropyValue


def condition(studentID, stype, sterm, type, termList, year, work, workList):

    if studentID.startswith('2010'):
        syear = '2010'
    else:
        syear = '2009'

    if syear == year and stype == type and sterm in termList and work in workList:
        return True
    else:
        return False


def getWorkDict(data,year,workList):

    worksDict={}
    for line in data:
        studentID = line[0].encode('utf-8')
        work = line[-1].encode('utf-8')
        if studentID.startswith('2010'):
            syear = '2010'
        else:
            syear = '2009'

        if syear == year and work in workList:
            worksDict.setdefault(work,set())
            worksDict[work].add(studentID)

    workNumDict = {}
    for work in worksDict:
        workNumDict[work] = len(worksDict[work])
    return workNumDict