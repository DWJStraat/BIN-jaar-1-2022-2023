# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:10:00 2022

@author: dstra
"""


number = int(input('Enter a number: '))
count = 1
for n in range(1, number + 1):
    count *= n
print (f'{number}! = {count}')