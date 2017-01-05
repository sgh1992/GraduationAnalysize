# !/usr/bin/python
#  -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
file = '/home/sghipr/bookBorrowAnalysize.csv'

def bookBorrowAnalysize(startIndex, classValueList, termList=[1, 2, 3, 4, 5, 6, 7, 8],year='2010'):
    fig,axes = plt.subplots(4,2,sharex=True,sharey=True,figsize=(8,12))
    for i in range(0,len(termList)):
        ax = axes[i/2,i%2]
        plt.sca(ax)
        term,countDict = classStudentDivide(startIndex, classValueList, termList[i],year)
        xList=[]
        yList=[]
        for x,y in sorted(countDict.items(),key=lambda x:x[0]):
            xList.append(x)
            yList.append(y)
        plt.plot(range(0,len(xList)),yList)





def classStudentDivide(startIndex, classValueList, term, year='2010'):
    data = [line.decode('utf-8').strip().split(',') for line in open(file)]
    countDict = dict()
    for line in data:
        swork = line[-1].encode('utf-8')
        studentID = line[0].encode('utf-8')
        sterm = int(line[1])
        if condition(studentID,swork,sterm,year,term,classValueList):
            countDict.setdefault(swork,0.0)
            sumValue = 0.0
            for i in range(startIndex, len(line) -1):
                sum += float(line[i])
            countDict[swork] += sumValue
    return term,countDict

def condition(studentID,swork,sterm,year,term,workList):
    if studentID.startswith('2010'):
        syear = '2010'
    elif studentID.startswith('29') or studentID.startswith('2009'):
        syear = '2009'
    else:
        syear = ''

    if syear == year and swork in workList and sterm == term:
        return True
    else:
        return False


