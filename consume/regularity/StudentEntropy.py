# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
import ConsumeRegularity as conRegu
import numpy as np

"""
计算学生的行为熵
包括学生食堂一日三餐的熵和宿舍洗澡消费时的熵等.
学生图书馆门禁行为的熵
"""

dataFile = 'D:/GraduationThesis/consumeRegularityWithWork.csv'

def figureEntropy(startIndex, type, termList, workList, year='2010', meal='breakfast'):
    """
    根据所给定的参数来计算其不同类群体学生的熵.
    meal在只有在计算type=mess时才有效.
    """
    data = [line.strip().decode('utf-8').split(',') for line in open(dataFile)]
    allTimeList = sorted(conRegu.getInteralTime('allMeal').keys()) #day
    #allTimeList = sorted(conRegu.getInteralTime('librarydoor').keys()) # weekCycle
    #allTimeList = sorted(conRegu.getWeekInteralTime().keys())
    if type != 'mess':
        if type == 'librarydoor':
            realTimeList = sorted(conRegu.getWeekInteralTime().keys())
        else:
            realTimeList = allTimeList[:]
    else:
        realTimeList = sorted(conRegu.getInteralTime(meal).keys())

    entropyDict = {}
    peopleNumDict = {}

    workNums = getWorkDict(data, year, workList)
    for item in workNums.items():
        print item[0].decode('utf-8'), item[1]

    meanDict,stdDict = figureMultipleDistribution(startIndex, type, termList, workList, year, meal)
    nums = 0

    entropyList = {}

    for line in data:
        studentID = line[0].encode('utf-8')
        work = line[-1].encode('utf-8')
        sterm = int(line[1])
        stype = line[2].encode('utf-8')
        if condition(studentID, stype, sterm, type, termList, year, work, workList):

            entropyDict.setdefault(work, {})
            entropyDict[work].setdefault(sterm, 0.0)

            peopleNumDict.setdefault(work, {})
            peopleNumDict[work].setdefault(sterm, set())

            entropyList.setdefault(sterm,{})
            entropyList[sterm].setdefault(work,[])

            flag, entropyValue = entropy(startIndex, line, allTimeList, realTimeList, work, sterm, meanDict, stdDict)

            entropyList[sterm][work].append(entropyValue)

            peopleNumDict[work][sterm].add(studentID)
            entropyDict[work][sterm] += entropyValue

            # if flag:
            #     peopleNumDict[work][sterm].add(studentID)
            #     entropyDict[work][sterm] += entropyValue
            # else:
            #     nums += 1

    plotEntropyDistribution(entropyList,termList,workList)
    print 'absoluate Nums', nums
    for work in peopleNumDict.keys():
        for term in termList:
            entropyValueList = entropyList[term][work]
            # for i in range(0,len(entropyValueList)):
            #     entropyValueList[i] = np.log(1.0 + entropyValueList[i])
            # meanValue = np.mean(entropyValueList)
            # stdValue = np.std(entropyValueList)
            # newList = []
            # num = 0
            # for value in entropyValueList:
            #     if value > meanValue + 2*stdValue or value < meanValue - 2*stdValue:
            #         num += 1
            #         continue
            #     newList.append(value)

            entropyDict[work][term] = np.mean(entropyValueList) #* workNums[work]/len(entropyValueList)
            #print 'term,work,num,entropy\t', term, work, num, entropyDict[work][term]
            #entropyDict[work][term] = entropyDict[work][term]/len(peopleNumDict[work][sterm]) #* (workNums[work]/(len(peopleNumDict[work][term]) + 0.0))
            # print term,work,entropyDict[work][term],len(peopleNumDict[work][term])

    if type == 'mess':
        return meal, entropyDict
    else:
        return type, entropyDict


def plotEntropyDistribution(entropyList,termList,workList):
    for term in termList:
        f, axes = plt.subplots(2, 2, sharey=True, sharex=True, figsize=(12, 9))
        for work,i in zip(workList,range(0,len(workList))):

            plt.sca(axes[i/2, i%2])
            valueList = entropyList[term][work]
            for i in range(0,len(valueList)):
                valueList[i] = np.log(valueList[i] + 1.0)
            plt.hist(valueList,bins=30,normed=True)
            plt.title(work.decode('utf-8'))
            plt.ylabel('Frequences')
            plt.grid(True)
            plt.tight_layout()
        result = 'D:/GraduationThesis/pictures/' + 'entropy_' + str(term) + '.pdf'
        f.savefig(result)


def getEntropyData(startIndex, type, termList, workList, year, meal):
    """
    获得数据
    """
    stype,entropyDict = figureEntropy(startIndex, type, termList, workList, year, meal)
    pd = DataFrame(entropyDict)
    print pd
    result = 'D:/GraduationThesis/Data/' + stype + '_entropy.csv'
    pd.to_csv(result)


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
    plt.xticks(range(1, len(xList) + 1), xList, fontsize = 9)
    plt.xlabel('term',fontsize=12)
    plt.ylabel('entropy',fontsize=12)
    #plt.title(stype)
    plt.legend(loc='best',prop={'size':9})
    plt.tight_layout()

    result = 'D:/GraduationThesis/pictures/' + stype + '_entropyWeek.pdf'
    plt.savefig(result)


def entropy(startIndex, line, allTimeList, realTimeList, work, term, meanDict, stdDict):
    """
    计算每个学期的熵.
    """
    valueList = []
    for i in range(startIndex, len(line) - 1):
        time = allTimeList[i - startIndex]
        if time in realTimeList:
            valueList.append(int(line[i]))

    sumValue = sum(valueList)
    flag = True
    if sumValue > meanDict[term][work] + 1 * stdDict[term][work] or sumValue < meanDict[term][work] - 1*stdDict[term][work]:
        flag = False

    entropyValue = 0.0
    for value in valueList:
        if value == 0:
            continue
        probs = (value + 0.0)/sum(valueList)
        entropyValue -= (probs) * np.log(probs)

    if entropyValue > 3.8:
        print entropyValue
    return flag, entropyValue


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


def figureDistribution(startIndex, type, term, work, year='2010', meal='allMeal'):

    data = [line.strip().decode('utf-8').split(',') for line in open(dataFile)]
    valueList = []
    allTimeInterals = sorted(conRegu.getInteralTime('allMeal').keys())
    if type == 'mess':
        realTimeInterals = sorted(conRegu.getInteralTime(meal).keys())
    else:
        realTimeInterals = allTimeInterals[:]

    for line in data:
        studentID = line[0].encode('utf-8')
        sterm = int(line[1])
        stype = line[2].encode('utf-8')
        swork = line[-1].encode('utf-8')
        if conditionDistribution(studentID, stype, sterm, swork, type, term, work, year):
            sumValue = 0
            for i in range(startIndex, len(line) - 1):
                time = allTimeInterals[startIndex-i]
                if time in realTimeInterals:
                    sumValue += int(line[i])
            valueList.append(sumValue)

    #print valueList
    print 'mean',term,type,work,np.mean(valueList)
    print 'standard devition',term,type,work,np.std(valueList)
    return valueList,np.mean(valueList),np.std(valueList)



def plotDistribution(startIndex, type, term, work, year='2010', meal='allMeal'):

    valueList,meanValue,stdValue = figureDistribution(startIndex, type, term, work, year, meal)

    plt.figure(figsize=(9, 6))
    plt.hist(valueList, bins=30, normed=True)
    plt.xlabel('count')
    plt.ylabel('probaility')
    result = str(term).decode('utf-8') + u',' + type.decode('utf-8') + u',' + work.decode('utf-8')
    plt.savefig('D:/GraduationThesis/pictures/' + result + '_Distribution.pdf')


def conditionDistribution(studentID, stype, sterm, swork, type, term, work, year):

    if studentID.startswith('2010'):
        syear = '2010'
    else:
        syear = '2009'

    if work == 'all': #代表取全体学生的均值与方差.
        work = swork

    if syear == year and stype == type and sterm == term and swork == work:
        return True
    else:
        return False

def conditionMultipleDistribution(studentID, stype, sterm, swork, type, termList, workList, year):

        if studentID.startswith('2010'):
            syear = '2010'
        else:
            syear = '2009'

        if syear == year and stype == type and sterm in termList and swork in workList:
            return True
        else:
            return False


def figureMultipleDistribution(startIndex, type, termList, workList, year='2010', meal='allMeal'):

    data = [line.strip().decode('utf-8').split(',') for line in open(dataFile)]
    valueDict = dict()
    allTimeInterals = sorted(conRegu.getInteralTime('allMeal').keys())
    if type == 'mess':
        realTimeInterals = sorted(conRegu.getInteralTime(meal).keys())
    else:
        realTimeInterals = allTimeInterals[:]

    for line in data:
        studentID = line[0].encode('utf-8')
        sterm = int(line[1])
        stype = line[2].encode('utf-8')
        swork = line[-1].encode('utf-8')
        if conditionMultipleDistribution(studentID, stype, sterm, swork, type, termList, workList, year):
            sumValue = 0
            for i in range(startIndex, len(line) - 1):
                time = allTimeInterals[startIndex-i]
                if time in realTimeInterals:
                    sumValue += int(line[i])

            valueDict.setdefault(swork,{})
            valueDict[swork].setdefault(sterm,[])
            valueDict[swork][sterm].append(sumValue)

    meanDict = dict()
    stdDict = dict()
    for term in termList:
        sumTermValueList = []
        meanDict.setdefault(term,{})
        stdDict.setdefault(term,{})
        for work in workList:
            meanDict[term][work] = np.mean(valueDict[work][term])
            stdDict[term][work] = np.std(valueDict[work][term])
            sumTermValueList += valueDict[work][term]

        meanDict[term]['all'] = np.mean(sumTermValueList)
        stdDict[term]['all'] = np.std(sumTermValueList)

    return meanDict,stdDict


    #print valueList
    # print 'mean',term,type,work,np.mean(valueList)
    # print 'standard devition',term,type,work,np.std(valueList)
    # return valueList,np.mean(valueList),np.std(valueList)