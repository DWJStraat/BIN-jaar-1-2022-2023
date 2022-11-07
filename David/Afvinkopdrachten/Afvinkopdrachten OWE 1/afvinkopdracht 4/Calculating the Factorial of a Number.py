# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:10:00 2022

@author: dstra
"""

number = int(input('Enter a number: '))
count = 1
n = 1
while n <= number:
    count = count * n
    n += 1
    
print (f'{number}! = {count}')