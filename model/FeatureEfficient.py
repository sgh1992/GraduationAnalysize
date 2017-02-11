# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np



def plotFeatureEfficient(microF1List,names):

    #plt.figure(figsize=(3,4))

    width = 0.3
    x = np.arange(len(microF1List)) + 1

    plt.barh(x,microF1List,width,color='green')
    plt.yticks(x+width/2,names)
    plt.xlabel('Micro-F1')
    #plt.ylabel('Features')

    plt.grid(True)
    plt.tight_layout()

    plt.savefig('D:/GraduationThesis/pictures/FeatureEfficient.pdf')