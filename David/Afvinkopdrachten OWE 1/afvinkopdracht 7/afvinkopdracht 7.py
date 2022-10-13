# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:41:23 2022

@author: dstra
"""


def CSV_reader(file_name):
    '''
    Reads a CSV file and outputs the content as a 2D list

    Parameters
    ----------
    file_name : Str
        Path of the CSV.

    Returns
    -------
    csv : 2D list
        A 2D list containing the contents of the CSV file.

    '''
    # Empty list
    csv = []
    with open(file_name) as file:
        # Scrolls through the file and adds all lines to a 2D list
        for line in file:
            line = line.replace("\n", "")
            csvline = line.split(',')
            csv.append(csvline)
    return csv


def Average_Column(index, CSV):
    '''
    Calculates the average of a column in a 2D list

    Parameters
    ----------
    index : Int
        The column to be analyzed.
    CSV : 2D list
        A 2D list to be analyzed.

    Returns
    -------
    average : Float
        The average of the column.

    '''
    counter = 0
    total = 0
    # Column how many rows the file has
    rows = len(CSV)
    # If the line contains anything that can be turned into a float, it does
    # so and adds 1 to the Counter
    for line in range(rows):
        try:
            total += float(CSV[line][index])
            counter += 1
        except:
            continue
    average = total / counter
    print(f'Average: {average:.4f}')

    return average


def Filter_Column(index, CSV, filter_float):
    '''
    Filters out all values smaller than the filter_float, and returns the IDs 
    (found in the first column) as a list, and prints the first 10 if 
    possible

    Parameters
    ----------
    index : Int
        The column to be filtered.
    CSV : 2D List
        The list the column can be found on.
    filter_int : Float
        The filter.

    Returns
    -------
    IDs : List
        List of all the IDs that were above the filter..

    '''
    rows = len(CSV)
    IDs = []
    for line in range(rows):
        try:
            num = float(CSV[line][index])
            if num >= filter_float:
                IDs.append(CSV[line][0])
        except:
            continue
    i = 0
    while i < 10:
        try:
            print(IDs[i])
            i += 1
        except:
            print(
                f'Couldn\'t print 10 lines; only {i} of the genes had a value higher than {filter_float}')
    return IDs


file = 'SC_expression.csv'
csv = CSV_reader(file)
a = Average_Column(1, csv)
IDs = Filter_Column(1, csv, 50)
