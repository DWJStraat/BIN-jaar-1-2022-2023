# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:00:51 2022

author: David Straat

function: 
"""


def read_VCF(file_name):
    '''
    Reads the VCF file for every other function.

    Parameters
    ----------
    file_name : Str
        The name of the file to be opened.

    Returns
    -------
    VCF : List
        The contents of the VCF file.

    '''
    # Sets an empty list
    VCF = []
    # Tries to open to file
    try:
        with open(file_name) as file:
            # If successful, the contents of the file will be put in a 2D list.
            for line in file:
                line = line.replace("\n", "")
                line = line.split('\t')
                VCF.append(line)
    except IOError:
        # If the file can't be opened, an error message will be printed.
        print('ERROR: File not found')
    # Returns the VCF list.
    return VCF


def total_a_t_mutations(file_name):
    '''
    Returns the amount of A to T mutations in the file provided.

    Parameters
    ----------
    file_name : Str
        The name of the file to be opened (see read_VCF).

    Returns
    -------
    count : Int
        The ammount of A to T mutations found.

    '''
    # Reads the file
    content = read_VCF(file_name)
    # Sets a count variable to 0
    count = 0
    # Tries to cycle through the content list
    try:
        # For each line in the content list, compares the 3rd and 4th elements.
        # If the 3rd is an A and the 4th is a T, adds 1 to the count.
        for line in content[1:]:
            if line[3] == 'A' and line[4] == 'T':
                count += 1
    except IndexError:
        # If the list is shorter than expected, returns an error
        print('ERROR: Index Error in total_a_t_mutations')
    # Returns the count variable.
    return count


def quality_below(file_name, quality=35):
    '''
    Returns the amout of mutations found in the file provided with qualities 
    below the "quality" variable

    Parameters
    ----------
    file_name : Str
        The name of the file to be opened (see read_VCF).
    quality : Int, optional
        The maximum quality of the mutations. The default is 35.

    Returns
    -------
    count : Int
        The amount of mutations with a quality below the specified quality.

    '''
    # Reads the file
    content = read_VCF(file_name)
    # Sets a count variable to 0
    count = 0
    # Tries to cycle through the content list
    try:
        # For each line in the content list, it tries to make the 5th element
        # an Integer. If successful, and the element is lower than the Quality
        # variable, adds 1 to the count. If it either can't turn the entry
        # into an integer or the entry is above Quality, the function continues.
        for line in content[1:]:
            try:
                qual = int(line[5])
                if qual < quality:
                    count += 1
            except:
                continue
    # If the code runs into an Index Error, returns an ERROR.
    except IndexError:
        print('ERROR: Index Error in quality_below')
    return count


def unique_filters(file_name):
    '''
    Makes a list of all unique filters found in the provided file.

    Parameters
    ----------
    file_name : Str
        The name of the file to be opened (see read_VCF).

    Returns
    -------
    filters : List
        A list with all the unique filters found in the provided file.

    '''
    # Reads the file
    content = read_VCF(file_name)
    # Creates an empty list called filters.
    filters = []
    # Tries to run through each line. If the 6th element is not in the filters
    # list, adds it to the list and continues.
    try:
        for line in content[1:]:
            if line[6] not in filters:
                filters.append(line[6])
    # If the code runs into an Index Error, returns an ERROR.
    except IndexError:
        print('ERROR: Index Error in unique_filters')
    return filters


def main(input_mode=False):
    '''
    Runs the code.

    Parameters
    ----------
    input_mode : Bool, optional
        If it is prefered to manually enter the file path, this boolean can be 
        set to True. The default is False.

    Returns
    -------
    None.

    '''
    # If it is desired to enter the file path manually and thus input_mode is
    # set to True, the file path can be entered here.
    if input_mode == True:
        file_name = input('Enter a file path:\n')
    else:
        # Otherwise, the default file path is chr1.vcf
        file_name = 'chr1.vcf'
    # Allows the entry of a maximum quality for quality_count. If an invalid
    # quality is entered, the quality_count function will default to 35.
    quality = input('Please enter a maximum quality (must be an integer):\n')
    # Exception handling in case the entry cannot be transformed into an
    # Integer.
    try:
        quality = int(quality)
    except:
        print(f'ERROR: Quality {quality} is not an integer. Defaulting to 35.')
    # Runs the functions
    a_t_count = total_a_t_mutations(file_name)
    quality_count = quality_below(file_name, quality)
    filters = unique_filters(file_name)
    # Prints the reults.
    print(f'The amount of A to T mutations equals: \n{a_t_count}')
    print(
        f'The amount of mutations with a quality below {quality} equals:\n{quality_count}')
    print(f'The unique filters are:\n{filters}')


# Change False to True if you want to manually input the file name on
# every run
main(False)
