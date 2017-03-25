# !/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

def analysize(file, classNatureSet, workSet, termSet):

    data = [line.decode('utf-8').split(',') for line in open(file)]
    title = data[0]
    titleArrays = []
    titleArrays.append('studentID')
    for name in title[1:-1]:
        arrays = name.split('_')
        term = int(arrays[0])
        classNature = arrays[1].encode('utf-8')
        statisName = arrays[2].encode('utf-8')
        xtuple = (term, classNature, statisName)
        titleArrays.append(xtuple)
    titleArrays.append('work')

    dataDict = dict()
    numsDict = dict()

    for line in data[1:]:
        sid = line[0].strip().encode('utf-8')
        work = line[-1].strip().encode('utf-8')
        numsDict.setdefault(work,0.0)
        numsDict[work] += 1
        for i in range(1, len(line) - 1):
            term = titleArrays[i][0]
            classNature = titleArrays[i][1]
            statisName = titleArrays[i][2]
            value = float(line[i])
            if value < 10:
                continue
            if term in termSet and work in workSet and classNature in classNatureSet and statisName == 'Average':
                dataDict.setdefault(term, {})
                dataDict[term].setdefault(work, {})
                dataDict[term][work].setdefault(classNature, [])
                dataDict[term][work][classNature].append(value)
    return dataDict,numsDict

def plotGradeTerms(file, classNatureSet, workSet, termList):

    dataDict,numsDict = analysize(file, classNatureSet, workSet, termList)
    fig, axes = plt.subplots(3, 2, figsize=(9, 8))
    for term in termList:
        data = dataDict[term]
        ax = axes[(term-1)/2, (term-1) % 2]

        if (term - 1)%2 == 0:
            singleFlag = True
        else:
            singleFlag = False

        if term == 2:
            legendFlag = True
        else:
            legendFlag = False

        plotSingleTerm(term, workSet, classNatureSet, ax, data, singleFlag, legendFlag,numsDict)

    #fig.tight_layout()
    fig.savefig('D:/GraduationThesis/pictures/Grades.pdf')

def plotSingleTerm(term, workSet, classNatureSet, ax, data, singleFlag, legendFlag,numsDict):

    plt.sca(ax)
    width = 0.2
    colors = ['b','g','r','c','m','y','k','w']
    print 'Term----', term

    for i in range(0, len(classNatureSet)):
        classNature = classNatureSet[i]
        workValues = []
        print 'ClassNature---', classNature
        for work in workSet:
            if classNature not in data[work] or len(data[work][classNature])/numsDict[work] < 0.5:
                average = 0.0
            else:
                average = np.mean(data[work][classNature])
            workValues.append(average)
        x = np.arange(len(workValues)) + i * width
        plt.bar(x, workValues, width=width, label = classNature.decode('utf-8'), color = colors[i])

    x = np.arange(len(workSet)) + len(classNatureSet)/2 * width
    newWorkList = []
    for work in workSet:
        newWorkList.append(work.decode('utf-8'))
    plt.xticks(x, newWorkList,fontsize=12)

    plt.title('term' + str(term),fontsize=12)
    if singleFlag:
        plt.ylabel('grades')
    if legendFlag:
        plt.legend(loc='best', prop={'size': 9})
    plt.grid(True)
    plt.tight_layout()

def zScore(gradeValues):
    meanValue = np.mean(gradeValues)
    stdValue = np.std(gradeValues)

    newValues = []

    for value in gradeValues:
        newValue = (value - meanValue)/stdValue
        newValues.append(newValue)
    return np.mean(newValues)


