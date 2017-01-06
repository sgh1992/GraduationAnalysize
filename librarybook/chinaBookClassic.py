# !/usr/bin/python
# -*- coding: utf-8 -*-


file = 'D:/GraduationThesis/chinaBookClassic.txt'

result = 'D:/GraduationThesis/chinaStandardBookClassic.csv'
writer = open(result,'w')

data = [line.strip().decode('utf-8').split('\t') for line in open(file)]
id=0
for line in data:
    callNum = line[1].encode('utf-8')
    type = line[2].encode('utf-8')
    id += 1
    writer.write(callNum + ',' + type + ',' + str(id))
    writer.write('\n')

writer.close()