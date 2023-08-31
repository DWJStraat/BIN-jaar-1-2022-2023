# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:03:50 2022

@author: dstra
"""

choice = [False,False,False]
a = input('Is anyone in your party a vegetarian? Y/N \n').upper()
b = input('Is anyone in your party a vegan? Y/N \n').upper()
c = input('Is anyone in your party gluten-free? Y/N \n').upper()

if a == "Y":
    choice[0] = True

if b == "Y":
    choice[1] = True

if c == "Y":
    choice[2] = True

print("Here are your restaurant options:")
if choice == [False, False, False]:
    print('Joe’s Gourmet Burgers')
if not choice[1]:
    print('Main Street Pizza Company')
print('Corner Café')
if not choice[1:2]:
    print('Mama’s Fine Italian')
print('The Chef’s Kitchen')