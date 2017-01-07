# !/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def estimate(file, startIndex, workList, year='2010'):
    data = [line.decode('utf-8').strip().split(',') for line in open(file)]
    valueDict = dict()
    for line in data:
        work = line[-1].encode('utf-8')
        studentID = line[0].encode('utf-8')
        if condition(studentID, work, year, workList):
            for i in range(startIndex,startIndex + 8):
                term = i - startIndex + 1
                valueDict.setdefault(term,dict())
                valueDict[term].setdefault(work,[])
                valueDict[term][work].append(float(line[i]))
    return valueDict

def plotSituation(file, startIndex,workList,year,type):
    valueDict = estimate(file,startIndex,workList,year)
    fig,axes = plt.subplots(4,2,figsize=(8,8))
    for term in range(0,8):
        plt.sca(axes[term/2,term%2])
        dataLists = []
        labelList = []
        workDict = valueDict[term + 1]
        for work, valueList in workDict.items():
            labelList.append(work.decode('utf-8'))
            dataLists.append(valueList)
        plt.boxplot(dataLists,sym='')
        plt.xticks(range(1,len(dataLists) + 1),labelList)
        plt.title('term' + str(term + 1))
        if term/2 == 1 and term % 2 == 0:
            plt.ylabel(type)
        plt.grid(True)
        plt.tight_layout()
    # fig.add_subplot(111, frameon=False)
    # # hide tick and tick label of the big axes
    # plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    # plt.ylabel("sumAmount")
    # plt.tight_layout()
    result = 'D:/GraduationThesis/pictures/' + type + '.pdf'
    fig.savefig(result)

def condition(studentID, work, year, workList):
    if studentID.startswith('2010'):
        syear = '2010'
    else:
        syear = '2009'

    if syear == year and work in workList:
        return True
    else:
        return False

