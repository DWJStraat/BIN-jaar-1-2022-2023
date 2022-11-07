# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:51:31 2022

@author: dstra
"""


def display_file_head(file_name):
    '''


    Parameters
    ----------
    file_name : Str.
        The name of the file to be opened. 

    Returns
    -------
    None.

    '''
    with open(file_name) as file:
        lines = ''
        for i in range(0, 5):
            line = file.readline()
            lines += line
        print(f'Printing first 5 lines of file {file_name}')
        print('-'*40)
        print(lines)


display_file_head()
