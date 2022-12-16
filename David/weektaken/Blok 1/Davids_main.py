# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:48:21 2022

@author: dstra

Function: 
"""
import Davids_functies as df


def compare(align=False, test=False, text=True, multimode=False):
    '''
    Runs the Compare option

    Parameters
    ----------
    align : Bool, optional
        Whether or not to use Needleman-Wunsch alignment. The default is False.
    test : Bool, optional
        Whether or not to enable Test mode. The default is False.
    text : Bool, optional
        Whether or not to output any colored text. The default is True.
    multimode : Bool, optional
        Whether or not to compare paired sequences or any amount of sequences. The default is False.

    Returns
    -------
    None.

    '''
    # Checks if Testmode is enabled
    if test == False:
        # Checks if Multimode is enabled
        if multimode == False:
            # Pair mode file entry
            try:
                entry1 = input('Please enter the first file path:\n')
            except IOError:
                print('ERROR, not a file')
            try:
                entry2 = input('Please enter the second file path:\n')
            except IOError:
                print('ERROR, not a file')

            # Runs a paired mode comparison
            comparison(entry1, entry2, align, text)
        else:
            # Multi mode entry
            entry = input(
                'Please enter any amount of file paths, separated by a |:\n')
            # Multi mode string to list
            entrylist = entry.split('|')
            # Runs paired comparison for each unique combination
            for i in range(len(entrylist)):
                for j in range(i+1, len(entrylist)):
                    comparison(entrylist[i], entrylist[j], align, text)
    else:
        # Test mode entry
        entry1 = 'gallus_gallus_protein.fna'
        entry2 = 'pseudomonas_protein.fna'


def comparison(entry1, entry2, align=False, text=True):
    '''
    Runs the main comparison stuff for the Compare function

    Parameters
    ----------
    entry1 : Str
        The first file to compare.
    entry2 : Str
        The second file to compare.
    align : Bool, optional
        Whether or not to use Needleman-Wunsch alignment. The default is False.
    text : Bool, optional
        Whether or not to output colored text. The default is True.

    Returns
    -------
    None.

    '''
    # Tries to read the file. If unable, throws an error
    try:
        string1 = df.read.fna(entry1)
    except IOError:
        print(f'ERROR, {entry1} is not a file')
    # Tries to read the second file. If unable, again, throws an error
    try:
        string2 = df.read.fna(entry2)
    except IOError:
        print(f'ERROR, {entry2} is not a file')
    # If alignment is enabled, runs a Needleman-Wunsch alignment algorithm
    if align == True:
        string1, string2 = df.compare.aligner(
            string1, string2, gap=10)
    out1, out2, overlap = df.compare.compare(string1, string2, True)
    if text == True:
        print(f'{entry1}:\n{out1}')
        print(f'{entry2}:\n{out2}')
    print(f'{entry1} and {entry2} overlap {overlap:.2f}%')



def analyze(test=False):
    '''
    Runs the Analyze part of the software

    Parameters
    ----------
    test : Bool, optional
        Whether or not to enable Test mode. The default is False.

    Returns
    -------
    None.

    '''
    if test == False:
        entry = input('Please enter a file path to a FASTA file:\n')
    else:
        entry = 'gallus_gallus_protein.fna'
    try:
        string = df.read.fna(entry)
    except IOError:
        print('ERROR, not a file')
    if df.identify.dna(string) == True:
        print('Input is DNA')
        print('-'*20)
        a, g, c, t, length = df.agct_count(string)
        gcp = (g+c)/length*100

        print(f'A:{a} \nG:{g}\nC:{c}\nT:{t}\nLength:{length}\nGC%:{gcp:.2f}%')
    else:
        print('Input is Protein')
        print('-'*20)
        d, e, r, k, length, charge = df.protein.derk_counter(string)
        dp = d/length*100
        ep = e/length*100
        rp = r / length*100
        kp = k/length*100
        weight = df.protein.weight(string)
        print(f'D%:{dp:.2f}%\nE%:{ep:.2f}%\nR%:{rp:.2f}%\nK%:{kp:.2f}%')
        print(f'Charge:{charge}\nWeight:{weight/1000:.1f}kDa')


def main():
    '''
    The main function.

    Returns
    -------
    None.

    '''
    choice = input('[A]nalyze or [C]ompare?\n')
    if choice.upper() == 'A':
        analyze()
    elif choice.upper() == 'C':
        choice2 = input(
            'Do you want to enable Needleman-Wunsch alignment? [Y]/[N]:\n')
        if choice2.upper() == 'Y':
            align = True
        elif choice2.upper() == 'N':
            align = False
        else:
            print('ERROR, not a valid choice')
        choice3 = input('[P]aired sequences or [M]ultiple sequences?\n')
        if choice3.upper() == 'P':
            compare(align, text=True, multimode=False)
        elif choice3.upper() == 'M':
            compare(align, text=False, multimode=True)
    else:
        print('ERROR, not a valid choice')


main()
