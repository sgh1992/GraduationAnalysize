# !/usr/bin/python
#  -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def plotTermChange(microF1List, macroF1List):
    """
    随着学期的变化，预测精度在逐渐增加.
    """
    x = np.arange(len(microF1List)) + 1

    plt.plot(x, microF1List, color='r', label ='Micro-F1')
    plt.plot(x, macroF1List, color='y', label ='Macro-F1')

    plt.xlabel('Term')
    plt.ylabel('F1')
    plt.grid(True)
    plt.legend(prop={'size':9})

    plt.tight_layout()
    plt.savefig('D:/GraduationThesis/pictures/TermChange.pdf')


