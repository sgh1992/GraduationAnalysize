# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def getF1Data(file):
    """
    根据交叉验证所得到的在各个学期的F1值来得到的结果.
    """
    data = [line.strip().decode('utf8').split(',') for line in open(file)]
    values = dict()
    for line in data:
        term = int(line[0])
        f1List = []
        for value in line[1:]:
            f1List.append(float(value))
        values[term] = f1List
    return values


def plotBars(mircoF1file, macrofile,classifierNames):

    mircoF1 = getF1Data(mircoF1file)
    macroF1 = getF1Data(macrofile)
    fig, axes = plt.subplots(3, 2,  figsize=(10, 6))

    for term in range(0,6):
        plotTerms(axes[term/2, term%2],term + 1, mircoF1[term + 1],macroF1[term + 1],classifierNames)
    fig.tight_layout()
    fig.savefig('D:/GraduationThesis/pictures/classifierCompares.pdf')



def plotTerms(ax,term,microF1List,macroF1List,classifierNames):

    plt.sca(ax)
    width = 0.3
    x = np.arange(len(microF1List))
    print 'micro',microF1List
    print 'macro',macroF1List

    plt.bar(x,microF1List,width,color='r')
    plt.bar(x+width,macroF1List,width,color='y')

    plt.ylabel('F1')
    plt.xticks(x + width,classifierNames)
    plt.legend(('Micro-F1','Macro-F1'),loc='best', fontsize = 'x-small')
    plt.title('term' + str(term))
    plt.grid(True)
    plt.tight_layout()







