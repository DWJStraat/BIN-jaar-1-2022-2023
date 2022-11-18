# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:16:28 2022

@author: dstra

Function: A collection of functions, written by David Straat

TODO:
    - update cutter
    - fix read.gpio
"""
import numpy
import qrcode
import cv2
from colorama import Fore
from colorama import Style


# from datetime import datetime


class Read:
    def fna(file_name):
        """
        Opens an FNA file, and returns the contents as a single string.

        Parameters
        ----------
        file_name : Str
            The path of the file to be opened.

        Returns
        -------
        string : Str
            The contents of the file, in a single string.

        """
        # Opens the file
        with open(file_name, 'r') as file:
            # Removes the header
            line = file.readlines()[1:]
            # Removes extra spaces and newlines
            string = ''.join(line).strip()
            string = ''.join(string.splitlines())
        return string

    def multiple_fna(file_name):
        """
        Opens a FNA file, and returns the contents as a list of strings
        separated at the headers.

        Parameters
        ----------
        file_name : Str
            The path of the file to be opened.

        Returns
        -------
        outlist : List
            The contents of the file, in a list of strings, separated at the
            headers.
        """
        with open(file_name, "r") as file:
            content = file.readlines()[1:]
            full_sequence = ""
            for line in content:
                if line[0] != ">":
                    full_sequence += line.strip()
                else:
                    full_sequence += "\n"
            outlist = full_sequence.split("\n")
        return outlist

    def CSV(file_name):
        """
        Opens a CSV file, and returns the contents as a list of lists.

        Parameters
        ----------
        file_name : Str
            The path of the file to be opened.

        Returns
        -------
        outlist : List
            The contents of the file, in a list of lists.
        """
        csv = []
        with open(file_name) as file:
            for line in file:
                line = line.replace("\n", "")
                csvline = line.split(',')
                csv.append(csvline)
        return csv

    # Currently broken as I can't find a way to install RPi.GPIO on Python
    #
    # def gpio(Pin, loops):
    #     """
    #     Opens a GPIO pin and reads the input, exporting the raw input as a
    #     string

    #     Parameters
    #     ----------
    #     Pin : Int
    #         The GPIO pin to read.
    #     loops : Int
    #         The amount of inputs the code should receive.

    #     Returns
    #     -------
    #     reader : Str
    #         The inputs the GPIO pin received.

    #     """
    #     reader = [[], []]
    #     RECEIVE_PIN = Pin

    #     GPIO.setmode(GPIO.BCM)
    #     GPIO.setup(RECEIVE_PIN, GPIO.IN)
    #     i = 0
    #     while i < loops:
    #         time = datetime.now()
    #         timestring = time.strftime('%f')
    #         reader[0].append(timestring)
    #         a = GPIO.input(RECEIVE_PIN)
    #         b = str(a)
    #         reader[1].append(b)
    #         i += 1
    #     return reader


def counter(string, list_of_parameters):
    """
    Counts each instance of the characters input in the list of 
    parameters, and inputs the counted number as a list.

    Parameters
    ----------
    string : Str
        The string to be analyzed.
    list_of_parameters : List
        A list containing all the strings whose instances will be counted.

    Returns
    -------
    count : List
        A list containing the (integer) counts of instances defined in 
        list_of_parameters.

    """
    count = []
    for parameter in list_of_parameters:
        no = string.count(parameter)
        count.append(no)
    return count


def agct_count(dna):
    """
    Counts the amount of A's, G's, C's and T's.

    Parameters
    ----------
    dna : Str
        The DNA to be examined.

    Returns
    -------
    a : Int
        The amount of Adenine bases in the DNA provided.
    g : Int
        The amount of Guanine bases in the DNA provided.
    c : Int
        The amount of Cytosine bases in the DNA provided.
    t : Int
        The amount of Thymine bases in the DNA provided.
    length : Int
        The length of the DNA string, counting only the bases counted above.

    """
    # Counts A's, G's, C's and T's
    count = counter(dna, ['A', 'C', 'G', 'T'])
    a = count[0]
    c = count[1]
    g = count[2]
    t = count[3]
    # Calculates the length
    length = a + g + c + t
    # Outputs the values
    return a, g, c, t, length


class RestrictionEnzyme:
    """
    This Class covers different functions that can be used to analyze DNA
    sequences, specifically about restriction enzymes.
    """

    def snip(string, site, snipspot):
        """
        Determines the places where a specific restrictor enzyme cut the DNA,
        and outputs the new, snipped DNA

        Parameters
        ----------
        string : Str
            The DNA to be examined.
        site : Str
            The site where the restrictor enzyme cuts the DNA.
        snipspot : Int
            How many bases from the start of the cutting site the restrictor
        enzyme cuts.

        Returns
        -------
        output : The "cut" DNA string, with a ^ on the spot where it cuts
        snips : The locations where the DNA has been cut

        """
        # Counts how often the restriction site appears in the string
        i = string.count(site)
        # Empty vars
        start = 0
        snips = []
        output = ''
        nextstart = 0
        # If at least 1 cutting site is present in the DNA, this loop will
        # cycle through the DNA, adds the location to a list, and inserts a ^
        # at the site
        if i > 0:
            while i > 0:
                snip = string.find(site, nextstart)
                output = string[start:snip - 1 + snipspot] + '^'
                snips.append(snip)
                i = i - 1
                nextstart = snip + snipspot
            output = output + string[snip - 1 + snipspot:]
        else:
            # If no sites are found, outputs the input
            output = string

        return output, snips

    def cutter(dna, enzymfile):
        """
        A function that can be used to process restriction enzymes found in
        a txt file on a string of DNA

        Parameters
        ----------
        dna : The string of DNA to be analyzed
        enzymfile : The txt file containing the names of the restriction
                    enzymes and their restriction site.
                    Example of formatting: DdeI C^TGAG

        Returns
        -------
        cutdna : The DNA after having been cut by the restriction enzymes
                 entered, in list format
        cuttingenzymes : The enzymes that cut the DNA, in list format

        """

        with open(enzymfile) as bestand:
            string = dna
            cuttingenzymes = []
            read = True
            while read:
                line = bestand.readline().strip()
                if line != '':
                    enzym, seq = line.split()
                    site = seq
                    site = site.replace("^", "")
                    sites = dna.count(site)
                    if sites > 0:
                        string = string.replace(site, seq)
                        cuttingenzymes.append(enzym)
                else:
                    read = False
            cutdna = string.split("^")
        return cutdna, cuttingenzymes


class Protein:
    def weight(protein):
        """
        This function calculates the weight of a protein

        Parameters
        ----------
        protein : Str
            A string of amino acids

        Returns
        -------
        weight : Int
            The weight of the input protein in Da

        """
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
        # Calculates the length of the protein and removes the weight of H2O
        # from the total weight
        length = len(protein)
        weight = weight - (18.0153 * (length - 1))
        return weight

    def derk_counter(protein):
        """


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

        """
        count = counter(protein, ['D', 'E', 'R', 'K'])
        d = count[0]
        e = count[1]
        r = count[2]
        k = count[3]
        length = len(protein)
        charge = r + k - d - e
        return d, e, r, k, length, charge


class QR:
    def generator(string, name):
        """
        This function generates a QR code based on the input in the working
        directory
        Uses qrcode

        Parameters
        ----------
        string : Str
            The string of text to be converted into QR
        name : Str
            The name of the QR image

        Returns
        -------
        None.

        """
        img = qrcode.make(string)
        type(img)
        img.save(f'{name}.png')

    def read(name):
        """
        This function reads a QR code and outputs as a string
        Uses cv2

        Parameters
        ----------
        name : Str
            The name of the QR code file

        Returns
        -------
        string : Str
            Output in string format

        """

        image = cv2.imread(name)
        detect = cv2.QRCodeDetector()
        string, points, qr = detect.detectAndDecode(image)
        return string


class Compare:
    def compare(string1, string2):
        """
        Compares two strings, colors the overlapping characters green,
        the others red, and calculates the overlap in % Uses Colorama

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

        """
        # Setting some empty variables
        out1 = ''
        out2 = ''
        i = 0
        compare = 0
        # Calculates the length of the longest string
        length = max(len(string1), len(string2))
        # Loops through each character in the strings
        while i < length:
            # If one string is shorter than the other, it'll compensate with
            # -'s to prevent a 'string index out of range'
            try:
                v1 = string1[i]
            except IndexError:
                v1 = "-"
            try:
                v2 = string2[i]
            except IndexError:
                v2 = "-"

            # If the character in both strings is the same, puts that
            # character in the output strings in green, and adds 1 to the
            # Compare variable
            if max(v1, v2) == min(v1, v2):
                out1 = out1 + colors.green(v1)
                out2 = out2 + colors.green(v2)
                compare += 1

            # If they are not the same, puts that character in the output
            # strings in red.
            else:
                out1 = out1 + colors.red(v1)
                out2 = out2 + colors.red(v2)

            # Move to next character
            i += 1

        # Calculate overlap in %
        overlap = compare / length * 100

        # Resets the coloring after each output string so it won't stain the
        # rest of the output
        out1 = out1 + f'{Style.RESET_ALL}'
        out2 = out2 + f'{Style.RESET_ALL}'

        return out1, out2, overlap

    def aligner(string1, string2, hit=1, miss=1, gap=1):
        """
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
            Gap penalty. The default is 1..

        Returns
        -------
        r1 : Str
            The first string, aligned with the second.
        r2 : Str
            The second string, aligned with the first.

        """
        n1 = len(string1)
        n2 = len(string2)
        # Score for each possible pair of characters
        score = numpy.zeros((n1 + 1, n2 + 1))
        score[:, 0] = numpy.linspace(0, -n1 * gap, n1 + 1)
        score[0, :] = numpy.linspace(0, -n2 * gap, n2 + 1)
        # Find optimal alignment
        aligner = numpy.zeros((n1 + 1, n2 + 1))
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
                temp[1] = score[i, j + 1] - gap
                temp[2] = score[i + 1, j] - gap
                tempmax = numpy.max(temp)
                score[i + 1, j + 1] = tempmax
                if temp[0] == tempmax:
                    aligner[i + 1, j + 1] += 2
                if temp[1] == tempmax:
                    aligner[i + 1, j + 1] += 3
                if temp[2] == tempmax:
                    aligner[i + 1, j + 1] += 4

        # Find an optimal alignment
        i = n1
        j = n2
        r1 = []
        r2 = []
        while i > 0 or j > 0:
            if aligner[i, j] in [2, 5, 6, 9]:
                r1.append(string1[i - 1])
                r2.append(string2[j - 1])
                i -= 1
                j -= 1
            elif aligner[i, j] in [3, 5, 7, 9]:
                r1.append(string1[i - 1])
                r2.append('-')
                i -= 1
            elif aligner[i, j] in [4, 6, 7, 9]:
                r1.append('-')
                r2.append(string2[j - 1])
                j -= 1
        # Reverse the strings
        r1 = ''.join(r1)[::-1]
        r2 = ''.join(r2)[::-1]
        return r1, r2

    def duploremover(a, b):
        """
        A function that removes elements found in both lists and return a list
        containing all unique values

        Parameters
        ----------
        a : List
            First list to be analyzed
        b : List
            Second list to be analyzed
        Returns
        -------
        pile : List
            A list containing only the unique values

        """
        pile = a + b
        pile = list(dict.fromkeys(pile))
        aset = set(a)
        bset = set(b)
        duplicates = list(set(max(aset, bset)).intersection(min(aset, bset)))
        for element in duplicates:
            pile.remove(str(element))
        return pile


def sentinel():
    run = True
    running = input('Would you like to continue? Y/N:').upper()
    if running == 'N':
        run = False
    return run


class identify:

    def dna(seq):
        """
        Checks if the input string is DNA

        Parameters
        ----------
        seq : Str
            input string

        Returns
        -------
        is_dna : Bool
            True or False

        """
        allowed = set('A' + 'C' + 'T' + 'G')
        if set(seq) <= allowed:
            is_dna = True
        else:
            is_dna = False
        return is_dna

    def prime(number):
        """
        Checks if the input number is prime

        Parameters
        ----------
        number : Int
            Input number

        Returns
        -------
        Is_Prime : Bool
            True or False
        """
        prime = True
        if number > 1:
            for number2 in range(2, number // 2):
                if number % number2:
                    prime = False
        return prime


class colors:
    def green(string):
        """
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

        """
        output = f'{Fore.GREEN}{Style.BRIGHT}{string}'
        return output

    def red(string):
        """
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

        """
        output = f'{Fore.RED}{Style.BRIGHT}{string}'
        return output


# Based on class examples


def line_counter(file):
    """
    This function is based on the code given as an example for the first
    function in the first programming test in the year 2022-2023

    Parameters
    ----------
    file : Name of the file

    Returns
    -------
    lines : Returns the number of lines.

    """
    lines = -1
    with open(file) as opened_file:
        # For every line in the file, increases the counter by 1 and prints the
        # line
        for line in opened_file:
            lines += 1
            line = line.replace("/n", "")
            print(line)
    print(lines)
    return lines


def greater_pc_percent_than(file_name, gc_perc=50):
    """
    Calculates how many of the genes in the file provided have a gc% higher
    than the percentage given

    Parameters
    ----------
    file_name : Str
        A CSV file containing multiple genes. GC% must be in the 5th collumn
    gc_perc : Int, optional
        The GC% filter the genes need to be above. The default is 50.

    Returns
    -------
    number_of_genes_higher_gc : Int
        The amount of genes above the gc_perc.

    """
    number_of_genes_higher_gc = 0
    with open(file_name) as file:
        first_line = file.readline()
        print(first_line)
        # For each line retrieves the GC%
        for line in file:
            line = line.replace("\n", '')
            information = line.split(',')
            # GC% is found in the fifth column
            gc_percentage = float(information[5])
            # Compares GC% and, if higher than the filter given in gc_perc,
            # increases the number_of_genes_higher_gc by 1
            if gc_percentage > gc_perc:
                number_of_genes_higher_gc += 1
    return number_of_genes_higher_gc


# CSV_Reader: See read.CSV

def primerDesign(fulldna, codingdna, mintemp=50, maxtemp=65, maxtemprange=4,
                 minsize=18, maxsize=25, startingpos=0):
    """
    Design a primer for the DNA provided

    Parameters
    ----------
    fullDNA : str
        The DNA sequence to be used
    codingdna : str
        The coding part of the DNA sequence
    mintemp : int
        The minimum temperature of the primer
    maxtemp : int
        The maximum temperature of the primer
    maxtemprange : int
        The maximum temperature range of the primer
    minsize : int
        The minimum size of the primer
    maxsize : int
        The maximum size of the primer
    startingpos : int
        The starting position of the primer

    Returns
    -------
    primerforward: str
        The forward primer, returned in format 5' [] 3'
    primerreverse: str
        The reverse primer, returned in format 5' [] 3'
    primertempforward: int
        The temperature of the forward primer
    primertempreverse: int
        The temperature of the reverse primer
    """

    temperature = {'A': 2, 'T': 2, 'G': 4, 'C': 4}
    reverse = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    intron_dna = fulldna.replace(codingdna, '\n')

    intron_dna = intron_dna.split('\n')

    intron_dna[0] = intron_dna[0][::-1]

    primertempforward = 0
    counterforward = 0
    primerforward = ''
    primertempreverse = 0
    counterreverse = 0
    primerreverse = ''
    for i in range(startingpos, min(len(intron_dna[0]), len(intron_dna[1]))):
        if abs(primertempforward - primertempreverse) < maxtemprange:
            primertempforward += temperature[intron_dna[0][i]]
            primerforward += reverse[intron_dna[0][i]]
            primertempreverse += temperature[intron_dna[1][i]]
            primerreverse += intron_dna[1][i]
            counterforward += 1
            counterreverse += 1
            if counterforward == maxsize or counterreverse == maxsize:
                break
            if counterforward > minsize and counterreverse > minsize:
                if primertempforward > mintemp and primertempreverse > mintemp:
                    if primertempforward < maxtemp and \
                            primertempreverse < maxtemp:
                        break
        else:
            if primertempforward < primertempreverse:
                primertempforward += temperature[intron_dna[0][i]]
                primerforward += reverse[intron_dna[0][i]]
                counterforward += 1
            else:
                primertempreverse += temperature[intron_dna[1][i]]
                primerreverse += intron_dna[1][i]
                counterreverse += 1
        if primertempforward + 4 >= maxtemp or \
                primertempreverse + 4 >= maxtemp:
            break
        if counterforward >= maxsize or counterreverse >= maxsize:
            break
    primerforward = primerforward[::-1]
    return primerforward, primerreverse, primertempforward, primertempreverse


class tutor_tasks:
    def weekopdracht_2(file):
        """
        This function takes the input file, and prints the GC% and length

        Parameters
        ----------
        file : The FASTA file to be examined

        Returns
        -------
        GC100 : The GC% of the gene in the FASTA file, in %
        length: The length of the gene in the FASTA file.

        """
        # Reads FNA file
        string = Read.fna(file)
        # Calculates values
        a, g, c, T, length = agct_count(string)
        GC = (g + c) / length
        # Outputs the GC% with 2 decimals
        GC100 = "{:.2f}".format(GC * 100)
        print(f'GC% = {GC100}%')
        # Prints length
        print(f"Length = {length}")
        return GC100, length

    def weekopdracht_3(file):
        """
        This function takes the input file, and prints the D, E, R, K and
        length

        Parameters
        ----------
        file : The FASTA file to be examined

        Returns
        -------
        length : The length of the protein in the FASTA file
        d : the count of D amino acids
        e : the count of E amino acids
        r : the count of R amino acids
        k : the count of K amino acids
        dp : the percentage of D amino acids in the protein
        ep : the percentage of E amino acids in the protein
        rp : the percentage of R amino acids in the protein
        kp : the percentage of K amino acids in the protein
        charge: the charge of the protein
        """
        string = Read.fna(file)
        d, e, r, k, length, charge = Protein.derk_counter(string)
        dp = d / length
        ep = e / length
        rp = r / length
        kp = k / length
        print(f'D:{d}, E:{e}, R:{r}, K:{k}')
        print(f'Length = {length}')
        print(f'Charge = {charge}')
        return length, d, e, r, k, dp, ep, rp, kp, charge

    def weektaak_4(file):
        string = Read.fna(file)
        weight = Protein.weight(string)
        return weight


class convert:
    def gpio_to_binary(gpio):
        """
        This code converts GPIO input to binary, with the assumption that 101
        = 1 and 100 = 0

        Parameters
        ----------
        gpio : GPIO input

        Returns
        -------
        binary : binary string

        """
        i = 0
        binary = []
        while i < len(gpio):
            if gpio[i] == '0':
                i += 1
            else:
                try:
                    if gpio[i + 2] == '1':
                        binary.append('1')
                    else:
                        binary.append('0')
                except IndexError:
                    break
                i += 3
        binary = ''.join(binary)
        return binary

    def binary_to_text(binary):
        """
        Converts binary input to string through the ASCII format.

        Parameters
        ----------
        binary : Binary input

        Returns
        -------
        text : string

        """
        binint = int(binary, 2)
        byte = binint.bit_length() + 7 // 8
        binarray = binint.to_bytes(byte, 'big')
        ascii_text = binarray.decode()
        text = ascii_text.strip('\x00')
        return text
