# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np




"""
模型有效性对比
"""
def plotEfficient(accuracyList):

    width = 0.3
    x = np.arange(len(accuracyList))

    names = ('random Guess', 'term1', 'term2', 'term3', 'term4', 'term5', 'term6')

    plt.figure(figsize=(8,5))
    plt.bar(x,accuracyList,width,color='green')
    plt.xticks(x+width/2,names)
    plt.ylabel('Accuracy')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('D:/GraduationThesis/pictures/ModelEfficient.pdf')




