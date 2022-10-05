# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:16:28 2022

@author: dstra

Function: A collection of functions, written by David Straat

TODO:
    - find a way to better group functions
    - remove Dutch comments
    - update cutter
"""
import qrcode
import cv2
from colorama import Fore
from colorama import Style
from datetime import datetime
import RPi.GPIO as GPIO


def read_fna(file_name):
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


def gpio_reader(Pin, loops):
    '''
    Opens a GPIO pin and reads the input, exporting the raw input as a string

    Parameters
    ----------
    Pin : Int
        The GPIO pin to read.
    loops : Int
        The amount of inputs the code should receive.

    Returns
    -------
    reader : Str
        The inputs the GPIO pin received.

    '''
    reader = [[], []]
    RECEIVE_PIN = Pin

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    i = 0
    while i < loops:
        time = datetime.now()
        timestring = time.strftime('%f')
        reader[0].append(timestring)
        a = GPIO.input(RECEIVE_PIN)
        b = str(a)
        reader[1].append(b)
        i += 1
    return reader


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


def snip(string, site, snipspot):
    '''
    Determines the places where a specific restrictor enzyme cut the DNA, and
    outputs the new, snipped DNA

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

    '''
    # Verandert de string naar uppercase
    string = string.upper()
    # Telt hoevaak de knip site voorkomt op de sequentie
    i = string.count(site)
    # Lege variabelen
    start = 0
    snips = []
    output = ''
    nextstart = 0
    # Als er tenminste 1 site aanwezig is, scant de While loop de sequentie,
    # returned de locaties van de sites, en stopt een ^ op de plaats van de
    # cut.
    if i > 0:
        while i > 0:
            snip = string.find(site, nextstart)
            output = string[start:snip-1+snipspot] + '^'
            snips.append(snip)
            i = i - 1
            nextstart = snip + snipspot
        output = output + string[snip-1+snipspot:]
    else:
        # Als er geen site aanwezig is, output de functie dezelfde string
        output = string

    return output, snips


def cutter(DNA, enzymfile):
    '''
    A function that can be used to process restriction enzymes found in a txt
    file on a string of DNA

    Parameters
    ----------
    DNA : The string of DNA to be analyzed
    enzymfile : The txt file containing the names of the restriction enzymes
                and their restriction site.
                Example of formatting: DdeI C^TGAG

    Returns
    -------
    cutDNA : The DNA after having been cut by the restriction enzymes entered,
             in list format
    cuttingenzymes : The enzymes that cut the DNA, in list format

    '''

    with open(enzymfile) as bestand:
        string = DNA
        cuttingenzymes = []
        read = True
        while read == True:
            line = bestand.readline().strip()
            if line != '':
                enzym, seq = line.split()
                site = seq
                site = site.replace("^", "")
                sites = DNA.count(site)
                if sites > 0:
                    string = string.replace(site, seq)
                    cuttingenzymes.append(enzym)
            else:
                read = False
        cutDNA = string.split("^")
    return cutDNA, cuttingenzymes


def duploremover(a, b):
    '''
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

    '''
    pile = a + b
    pile = list(dict.fromkeys(pile))
    aset = set(a)
    bset = set(b)
    duplicates = list(set(max(aset, bset)).intersection(min(aset, bset)))
    for element in duplicates:
        pile.remove(str(element))
    return pile


def protein_weight(protein):
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


def qr_generator(string, name):
    '''
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

    '''
    img = qrcode.make(string)
    type(img)
    img.save(f'{name}.png')


def qr_read(name):
    '''
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

    '''

    image = cv2.imread(name)
    detect = cv2.QRCodeDetector()
    string, points, qrcode = detect.detectAndDecode(image)
    return string


def compare(string1, string2):
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
            out1 = out1 + colors.green(v1)
            out2 = out2 + colors.green(v2)
            compare += 1

        # If they are not the same, puts that character in the output strings
        # in red.
        else:
            out1 = out1 + colors.red(v1)
            out2 = out2 + colors.red(v2)

        # Move to next character
        i += 1

    # Calculate overlap in %
    overlap = compare/length*100

    # Resets the coloring after each output string so it won't stain the rest
    # of the output
    out1 = out1 + f'{Style.RESET_ALL}'
    out2 = out2 + f'{Style.RESET_ALL}'

    return out1, out2, overlap


def is_prime(number):
    prime = True
    if number > 1:
        for number2 in range(2, number//2):
            if number % number2:
                prime = False
    return prime


def sentinel():
    run = True
    running = input('Would you like to continue? Y/N:').upper()
    if running == 'N':
        run = False
    return run


def is_dna(seq):
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

# Based on class examples


def line_counter(file):
    '''
    This function is based on the code given as an example for the first
    function in the first programming test in the year 2022-2023

    Parameters
    ----------
    file : Name of the file

    Returns
    -------
    counter : Returns the number of lines.

    '''
    counter = -1
    with open(file) as opened_file:
        # For every line in the file, increases the counter by 1 and prints the
        # line
        for line in opened_file:
            counter += 1
            line = line.replace("/n", "")
            print(line)
    print(counter)
    return(counter)


class tutor_tasks:
    def weekopdracht_2(file):
        '''
        This function takes the input file, and prints the GC% and length

        Parameters
        ----------
        file : The FASTA file to be examined

        Returns
        -------
        GC100 : The GC% of the gene in the FASTA file, in %
        length: The length of the gene in the FASTA file.

        '''
        # Leest de FNA file opgegeven
        string = read_fna(file)
        # Berekent de waardes
        A, G, C, T, length = agct_count(string)
        GC = (G+C)/length
        # Output de GC% met 2 decimalen achter de komma
        GC100 = "{:.2f}".format(GC*100)
        print(f'GC% = {GC100}%')
        # Print de lengte
        print(f"Lengte = {length}")
        return GC100, length

    def weekopdracht_3(file):
        '''
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
        '''
        string = read_fna(file)
        d = string.count("D")
        e = string.count("E")
        r = string.count("R")
        k = string.count("K")
        length = len(string)
        dp = d / length
        ep = e / length
        rp = r / length
        kp = k / length
        charge = r + k - d - e
        print(f'D:{d}, E:{e}, R:{r}, K:{k}')
        print(f'Lengte = {length}')
        print(f'Lading = {charge}')
        return length, d, e, r, k, dp, ep, rp, kp, charge

    def weektaak_4(file):
        string = read_fna(file)
        weight = protein_weight(string)
        return weight


class converters:
    def gpio_to_binary(GPIO):
        '''
        This code converts GPIO input to binary, with the assumption that 101
        = 1 and 100 = 0

        Parameters
        ----------
        GPIO : GPIO input

        Returns
        -------
        binary : binary string

        '''
        i = 0
        binary = []
        while i < len(GPIO):
            if GPIO[i] == '0':
                i += 1
            else:
                try:
                    if GPIO[i+2] == '1':
                        binary.append('1')
                    else:
                        binary.append('0')
                except IndexError:
                    break
                i += 3
        binary = ''.join(binary)
        return binary

    def binary_to_text(binary):
        '''
        Converts binary input to string through the ASCII format.

        Parameters
        ----------
        binary : Binary input

        Returns
        -------
        text : string

        '''
        binint = int(binary, 2)
        byte = binint.bit_length() + 7 // 8
        binarray = binint.to_bytes(byte, 'big')
        ascii_text = binarray.decode()
        text = ascii_text.strip('\x00')
        return text
