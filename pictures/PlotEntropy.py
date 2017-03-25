# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def plotE():

    x1 = np.linspace(0,0.5,25)
    x2 = np.linspace(0.5,1,25)
    x = list(x1)[:-1] + list(x2)

    y = []

    for v in x:

        if v in [0, 1]:
            y.append(0.0)
        else:
            value = -v * np.log2(v) - (1-v)*np.log2(1-v)
            y.append(value)

    plt.figure()
    plt.grid()
    plt.plot(x,y)
    plt.xlabel(u'p')
    plt.ylabel(u'H(X)')
    plt.tight_layout()

    plt.savefig('D:/GraduationThesis/pictures/entropyPlot.pdf')