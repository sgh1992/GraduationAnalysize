# !/usr/bin/python
#  -*- coding: utf-8 -*-

import CrossValidationModelChoose as CV

microF1File = "D:/GraduationThesis/ClassifierCompareMicro.csv"
macroFile = "D:/GraduationThesis/ClassifierCompareMacro.csv"

classifierNames = ['LR','RF','AdaBoost','SVM','NN','DT']

CV.plotBars(microF1File,macroFile,classifierNames)