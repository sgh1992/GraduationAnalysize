# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plotEntropy(file,name):

    data = [line.strip().decode('utf-8').split(',') for line in open(file)]

    valuesDict = dict()

    for line in data:

        work = line[0]
        values = []
        for value in line[1:]:
            values.append(float(value))
        valuesDict[work] = values

    #plt.figure(figsize=(3, 3))
    for work, values in valuesDict.items():
        plt.plot(range(1, len(values) + 1), values, label = work)

    plt.xlabel('term', fontsize=12)
    plt.ylabel('entropy', fontsize=12)
    plt.legend(loc='best', prop={'size': 9})
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('D:/GraduationThesis/pictures/' + name + '.pdf')