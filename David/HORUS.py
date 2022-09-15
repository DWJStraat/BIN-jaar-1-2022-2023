# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:16:28 2022

@author: dstra

Function: A collection of functions, written by David Straat
"""

# Opent een FNA file en verwijdert de header, en output de file als een string
def readfna(file):
    '''
    This function takes a file, removes the first line, and outputs the contents as a single string.
    
    Parameters
    ----------
    file : The FASTA file to be examined
    
    Returns
    -------
    string : The string of (probably) genetic code contained within the FASTA file.
    '''
    with open(file, 'r') as file:
        line = file.readlines()[1:]
        string = ''.join(line).strip()
        return string

# Neemt de string en telt de A, C, G, en T, berekent de totale lengte en percentages, en output dit  
def AGCTcount(string):
    '''
    This function counts the A, G, C, and T in the gene provided. 

    Parameters
    ----------
    string : A string containing A, G, C, and T

    Returns
    -------
    A : The amount of A in the string
    G : The amount of G in the string
    C : The amount of C in the string
    T : The amount of T in the string
    length : The length of the gene 

    '''
    #Telt de A C G en T
    A = string.count('A')
    G = string.count('G')
    C = string.count('C')
    T = string.count('T')
    # Berekent de lengte
    length = A+G+C+T
    # Output de waardes
    return A, G, C, T, length

def typeidentify(string):
    '''
    This function determines the type of the input string: DNA or Protein

    Parameters
    ----------
    string : The string to be examined

    Returns
    -------
    type : Either "DNA" or "Protein"

    '''
    i = 0
    scan = False
    while i <= 25 and scan == False:
        if string[i] == 'M':
            type = "Protein"
            scan = True
        elif string[i] in ["A","G","C","T"]:    
            type = "DNA"
            scan = True
        else:
            i = i + 1

    if scan == False:
        print ("Not recognized as a gene or protein.")
    print(type)
    return type

def GCpercent(C,G,length):
    '''
    This function calculates the GC% of the gene

    Parameters
    ----------
    C : The amount of C in the gene
    G : The amount of G in the gene
    length : The length of the gene

    Returns
    -------
    GC : The GC% of the gene

    '''
    # Berekent de A%, G%, C%, en T%
    Gp = G/length
    Cp = C/length
    # Berekent GC% en AT%
    GC = Gp + Cp
    return GC


# Voert de opdracht uit
def weekopdracht2(file):
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
    string = readfna(file)
    #Berekent de waardes
    A, G, C, T, length = AGCTcount(string)
    GC=GCpercent(G, C, length)
    # Output de GC% met 2 decimalen achter de komma
    GC100 = "{:.2f}".format(GC*100)
    print(f'GC% = {GC100}%')
    # Print de lengte
    print(f"Lengte = {length}")
    return GC100, length

def weekopdracht3(file):
    '''
    This function takes the input file, and prints the D, E, R, K and length

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
    string = readfna(file)
    d= string.count("D")
    e= string.count("E")
    r= string.count("R")
    k= string.count("K")
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
        
def PCRGCcalc(GC, length):
    '''
    

    Parameters
    ----------
    GC : The GC% of the gene, in 0.xxx
    length : The length of the gene

    Returns
    -------
    meltingtemp : The temperature at which the DNA denaturates into two strings in degrees Celsius

    '''
    totalGC = GC*length
    totalAT = length - totalGC
    meltingtemp = 4*totalGC + 2*totalAT
    return meltingtemp
