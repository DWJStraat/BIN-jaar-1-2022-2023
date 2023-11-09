# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:08:45 2022

@author: dstra

Function: Write a specified amount of random numbers into a specified file
"""

import random


def random_writer(file_name, number):
    '''
    Writes a specified number of random numbers into the specified file.

    Parameters
    ----------
    file_name : Str
        The name of the file to be written into.
    number : Int
        The amount of random numbers to be written into the file.

    Returns
    -------
    None.

    '''
    try:
        with open(file_name, 'a') as file:
            for _ in range(number):
                random_num = str(random.randint(1, 500)) + '\n'
                file.write(random_num)
    except FileNotFoundError:
        print(f'ERROR, "{file_name}" doesn\'t exist.')


def main():
    '''
    Provides the input for the random_writer function

    Returns
    -------
    None.

    '''
    file_name = input('Please enter a file path:\n')
    number = input('Please enter how many numbers should be entered:\n')
    try:
        number = int(number)
        random_writer(file_name, number)
    except:
        print('ERROR, {number} is not a number.')


main()
