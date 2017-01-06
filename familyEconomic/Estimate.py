# !/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt



def estimate(file, startIndex, year='2010'):

    data = [line.decode('utf-8').strip().split(',') for line in open(file)]
