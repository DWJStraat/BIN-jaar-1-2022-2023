# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:07:08 2022

@author: dstra

Function: Enter 20 numbers, and calculates the following:
            - lowest number
            - highest number
            - total of the numbers
            - average of the numbers
"""


def number_entry():
    '''
    Allows the user to enter 20 numbers into the console. Runs a check if each
    number is an integer, and if so, puts them into a list.

    Returns
    -------
    num_list : List of numbers entered

    '''
    num_list = []
    numbers = 0
    print('Please enter 20 numbers:')
    while numbers < 20:
        new_number = input()
        try:
            entry = int(new_number)
            numbers += 1
            num_list.append(entry)
        except ValueError:
            print('ERROR: not a number, try again')
            continue
    return num_list


def main():
    '''
    Enter 20 numbers, and calculates the following:
                - lowest number
                - highest number
                - total of the numbers
                - average of the numbers

    Returns
    -------
    None.

    '''
    num_list = number_entry()
    num_length = len(num_list)
    num_sum = sum(num_list)
    average = num_sum/num_length
    num_max = max(num_list)
    num_min = min(num_list)

    print(f'Lowest number:          {num_min}')
    print(f'Highest number:         {num_max}')
    print(f'Total of the numbers:   {num_sum}')
    print(f'Average of the numbers: {average}')


main()
