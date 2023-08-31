# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:50:10 2022

@author: dstra
"""
i = 0
bugs = 0
while i < 5:
    bugstoday = int(input('How many bugs did you collect today?\n'))
    bugs += bugstoday
    i += 1

print(f'You collected {bugs} bugs the last 5 days')