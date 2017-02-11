# !/usr/bin/python
#  -*- coding: utf-8 -*-

import CrossValidationModelChoose as CV
import TermChange as TC
import ModelEfficient as ME
import FeatureEfficient as FE

# microF1File = "D:/GraduationThesis/ClassifierCompareMicro.csv"
# macroFile = "D:/GraduationThesis/ClassifierCompareMacro.csv"
#
# classifierNames = ['LR','RF','AdaBoost','SVM','NN','DT']
#
# CV.plotBars(microF1File,macroFile,classifierNames)




#Term Change

# microF1List = [0.635,0.655,0.693,0.691,0.721,0.776]
# macroF1List = [0.516,0.571,0.591,0.587,0.686,0.713]
#
# TC.plotTermChange(microF1List,macroF1List)


#Model Efficient
# accuracyList = [0.448,0.569,0.603,0.642,0.683,0.712,0.759]
# ME.plotEfficient(accuracyList)

#Feature Efficient
microF1List = [0.726,0.669,0.601,0.621]
names = [u'专业能力',u'在校行为行为规律性',u'图书借阅兴趣',u'家庭经济条件']
FE.plotFeatureEfficient(microF1List,names)





