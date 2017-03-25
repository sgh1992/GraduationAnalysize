# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def plotLR():

    x = np.linspace(-3,3,60)
    y = []

    for v in x:
        value = 1 / (1 + np.exp(-2*v))
        y.append(value)

    plt.figure()
    plt.plot(x, y)
    plt.grid(True)

    plt.savefig('D:/GraduationThesis/pictures/LR.pdf')



