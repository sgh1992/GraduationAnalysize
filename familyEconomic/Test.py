# !/usr/bin/python
#  -*- coding: utf-8 -*-

import Estimate as Es
import matplotlib.pyplot as plt

file = 'D:/GraduationThesis/consumeDayAndAmount.csv_addWork.csv'
startIndex = 17
year = '2010'
workList = ['就业','录研', '出国深造', '其它']
type = 'averageDayPays'
Es.plotSituation(file,startIndex,workList,year,type)



# fig, axes = plt.subplots(3, 4, sharex=True, sharey=True)
# # add a big axes, hide frame
# fig.add_subplot(111, frameon=False)
# # hide tick and tick label of the big axes
# plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
# plt.xlabel("common X")
# plt.ylabel("common Y")
# plt.show()