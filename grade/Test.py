# !/usr/bin/python
# -*- coding: utf-8 -*-

import AnalysizeGrade as AG

file = 'D:/GraduationThesis/studentGradeTermAnalysize2010WithWork.csv'
workList = ['就业', '录研', '出国深造', '其它']
classNatureList = ['公共基础课', '学科基础课', '专业核心课']#, '专业选修课', '任意选修课', '素质教育选修课', '创新学分'
termList = [1,2,3,4,5,6]

AG.plotGradeTerms(file, classNatureList, workList, termList)