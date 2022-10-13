# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:58:44 2022

@author: dstra
"""


def sum_of_file(file_name):
    '''
    Opens a file and calculates the total of the numbers found within

    Parameters
    ----------
    file_name : Str
        The name of the file to be opened. 

    Returns
    -------
    None.

    '''
    file_sum = 0
    with open(file_name) as file:
        for line in file:
            number = line
            try:
                number = int(number)
            except:
                print(f'"{line.strip()}" is not a number. Skipping.')
                continue
            file_sum += number
    print('-'*40)
    print(f'The calculated total is {file_sum}')


sum_of_file()
