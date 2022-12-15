# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:45:19 2022

@author: dstra

Function: Function bin for Davids_main.py
"""
import numpy
from colorama import Fore
from colorama import Style


class protein:
    def weight(protein):
        '''
        This function calculates the weight of a protein

        Parameters
        ----------
        protein : Str
            A string of amino acids

        Returns
        -------
        weight : Int
            The weight of the input protein in Da

        '''
        # Removes the \n from the input string
        protein = ''.join(protein.splitlines())
        # Sets the weight integer to 0
        weight = 0
        # Creates a dictionary with the molecular weights of each amino acid
        table = {
            'A': 89.09, 'C': 121.2, 'D': 133.1, 'E': 147.1, 'F': 165.2,
            'G': 75.07, 'H': 155.2, 'I': 131.2, 'K': 146.2, 'L': 131.2,
            'M': 149.2, 'N': 132.1, 'P': 115.1, 'Q': 146.1, 'R': 174.2,
            'S': 105.09, 'T': 119.1, 'V': 117.1, 'W': 204.2, 'Y': 181.2
        }
        # For each amino acid, compares the abbreviation of the amino acid with
        # the weight found in the table dictionary, and adds the weight to the
        # weight variable
        for i in protein:
            weight += table[i]
        # Calculates the length of the protein and removes the weight of H2O from
        # the total weight
        length = len(protein)
        weight = weight - (18.0153*(length-1))
        return weight

    def derk_counter(protein):
        '''


        Parameters
        ----------
        protein : Str
            The protein code to be examined.

        Returns
        -------
        d : Int
            The amount of Aspartic Acid in the protein.
        e : Int
            The amount of Glutamic Acid in the protein.
        r : Int
            The amount of Arganine in the protein.
        k : Int
            The amount of Lysine in the protein.
        length : Int
            The length of the protein.
        charge : Int
            The charge of the protein, based on the D, E, R, and K counts.

        '''
        d = protein.count("D")
        e = protein.count("E")
        r = protein.count("R")
        k = protein.count("K")
        length = len(protein)
        charge = r + k - d - e
        return d, e, r, k, length, charge


def agct_count(DNA):
    '''
    Counts the amount of A's, G's, C's and T's.

    Parameters
    ----------
    string : Str
        The DNA to be examined.

    Returns
    -------
    A : Int
        The amount of Adenine bases in the DNA provided.
    G : Int
        The amount of Guanine bases in the DNA provided.
    C : Int
        The amount of Cytosine bases in the DNA provided.
    T : Int
        The amount of Thymine bases in the DNA provided.
    length : Int
        The length of the DNA string, counting only the bases counted above.

    '''
    # Counts A's, G's, C's and T's
    A = DNA.count('A')
    G = DNA.count('G')
    C = DNA.count('C')
    T = DNA.count('T')
    # Calculates the length
    length = A+G+C+T
    # Outputs the values
    return A, G, C, T, length


class read:
    def fna(file_name):
        '''
        Opens a FNA file, and returns the contents as a single string.

        Parameters
        ----------
        file_name : Str
            The path of the file to be opened.

        Returns
        -------
        string : Str
            The contents of the file, in a single string.

        '''
        # Opens the file
        with open(file_name, 'r') as file:
            # Removes the header
            line = file.readlines()[1:]
            # Removes extra spaces and newlines
            string = ''.join(line).strip()
            string = ''.join(string.splitlines())
        return string


class compare:
    def compare(string1, string2, color=False):
        '''
        Compares two strings, colors the overlapping characters green, the others
        red, and calculates the overlap in %
        Uses Colorama

        Parameters
        ----------
        string1 : Str
            Input string 1
        string2 : Str
            Input string 2

        Returns
        -------
        out1 : Str
            Input string 1 but now colored
        out2 : Str
            Input string 2 but now colored
        overlap : Int
            The overlap in %

        '''
        # Setting some empty variables
        out1 = ''
        out2 = ''
        i = 0
        compare = 0
        # Calculates the length of the longest string
        length = max(len(string1), len(string2))
        # Loops through each character in the strings
        while i < length:
            # If one string is shorter than the other, it'll compensate with -'s
            # to prevent a 'string index out of range'
            try:
                v1 = string1[i]
            except:
                v1 = "-"
            try:
                v2 = string2[i]
            except:
                v2 = "-"

            # If the character in both strings is the same, puts that character in
            # the output strings in green, and adds 1 to the Compare variable
            if max(v1, v2) == min(v1, v2):
                if color == True:
                    out1 = out1 + colors.green(v1)
                    out2 = out2 + colors.green(v2)
                else:
                    out1 += v1
                    out2 += v2
                compare += 1

            # If they are not the same, puts that character in the output strings
            # in red.
            else:
                if color == True:
                    out1 = out1 + colors.red(v1)
                    out2 = out2 + colors.red(v2)
                else:
                    out1 += v1
                    out2 += v2

            # Move to next character
            i += 1

        # Calculate overlap in %
        overlap = compare/length*100

        # Resets the coloring after each output string so it won't stain the rest
        # of the output
        out1 = out1 + f'{Style.RESET_ALL}'
        out2 = out2 + f'{Style.RESET_ALL}'

        return out1, out2, overlap

    def aligner(string1, string2, hit=1, miss=1, gap=1):
        '''
        This piece of code runs a simplified version of the Needleman-Wunsch 
        algorithm

        Credit to slowkow ( profile: https://gist.github.com/slowkow ) for his 
        original code

        Parameters
        ----------
        string1 : Str
            The first string to be aligned.
        string2 : Str
            The second string to be aligned.
        hit : Int, optional
            Hit reward. The default is 1.
        miss : Int, optional
            Miss penalty. The default is 1.
        gap : Int, optional
            Gap penalty. The default is 1.

        Returns
        -------
        r1 : Str
            The first string, aligned with the second.
        r2 : Str
            The second string, aligned with the first.

        '''
        n1 = len(string1)
        n2 = len(string2)
        # Score for each possible pair of characters
        score = numpy.zeros((n1 + 1, n2 + 1))
        score[:, 0] = numpy.linspace(0, -n1 * gap, n1 + 1)
        score[0, :] = numpy.linspace(0, -n2 * gap, n2 + 1)
        # Find optimal alignment
        aligner = numpy.zeros((n1+1, n2+1))
        aligner[:, 0] = 3
        aligner[0, :] = 4
        # Temporary scores
        temp = numpy.zeros(3)
        for i in range(n1):
            for j in range(n2):
                if string1[i] == string2[j]:
                    temp[0] = score[i, j] + hit
                else:
                    temp[0] = score[i, j] - miss
                temp[1] = score[i, j+1] - gap
                temp[2] = score[i+1, j] - gap
                tempmax = numpy.max(temp)
                score[i+1, j+1] = tempmax
                if temp[0] == tempmax:
                    aligner[i+1, j+1] += 2
                if temp[1] == tempmax:
                    aligner[i+1, j+1] += 3
                if temp[2] == tempmax:
                    aligner[i+1, j+1] += 4

        # Find an optimal alignment
        i = n1
        j = n2
        r1 = []
        r2 = []
        while i > 0 or j > 0:
            if aligner[i, j] in [2, 5, 6, 9]:
                r1.append(string1[i-1])
                r2.append(string2[j-1])
                i -= 1
                j -= 1
            elif aligner[i, j] in [3, 5, 7, 9]:
                r1.append(string1[i-1])
                r2.append('-')
                i -= 1
            elif aligner[i, j] in [4, 6, 7, 9]:
                r1.append('-')
                r2.append(string2[j-1])
                j -= 1
        # Reverse the strings
        r1 = ''.join(r1)[::-1]
        r2 = ''.join(r2)[::-1]
        return r1, r2


class identify:

    def dna(seq):
        '''
        Checks if the input string is DNA

        Parameters
        ----------
        seq : Str
            input string

        Returns
        -------
        Is_DNA : Bool
            True or False

        '''
        allowed = set('A'+'C'+'T'+'G')
        if set(seq) <= allowed:
            Is_DNA = True
        else:
            Is_DNA = False
        return Is_DNA


class colors:
    def green(string):
        '''
        Makes input bright green
        Uses Colorama

        Parameters
        ----------
        string : Str
            Input

        Returns
        -------
        output : Str
            Green output string

        '''
        output = f'{Fore.GREEN}{Style.BRIGHT}{string}'
        return output

    def red(string):
        '''
        Makes input bright red
        Uses Colorama

        Parameters
        ----------
        string : Str
            Input 

        Returns
        -------
        output : Str
            Red output string

        '''
        output = f'{Fore.RED}{Style.BRIGHT}{string}'
        return output
