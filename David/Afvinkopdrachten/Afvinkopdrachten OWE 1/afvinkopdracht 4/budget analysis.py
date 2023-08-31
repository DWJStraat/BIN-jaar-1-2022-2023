# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:02:51 2022

@author: dstra
"""

run = True
budget = int(input('What is your monthly budget?\n'))
loss = 0

while run:
    expense = int(input('What were your expenses today?\n'))
    loss += expense
    run = input('Continue? [Y/N]').upper() == "Y"
print(f'Your expenses were {loss} / {budget}.')
if loss > budget:
    print(f'You went {loss-budget} over budget.')
elif budget > loss:
    print(f'You have {budget-loss} left.')