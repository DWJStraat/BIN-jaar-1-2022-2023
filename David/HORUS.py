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

def snip(string, site, snipspot):
    '''
    Determines the places where a specific restrictor enzyme cut the DNA, and outputs the new, snipped DNA

    Parameters
    ----------
    string : The DNA to be examined.
    site : The site where the restrictor enzyme cuts the DNA.
    snipspot : How many bases from the start of the cutting site the restrictor enzyme cuts.
    
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
    # Als er tenminste 1 site aanwezig is, scant de While loop de sequentie, returned 
    # de locaties van de sites, en stopt een ^ op de plaats van de cut.
    if i > 0:
        while i > 0 :
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
    A function that can be used to process restriction enzymes found in a txt file on a string of DNA

    Parameters
    ----------
    DNA : The string of DNA to be analyzed
    enzymfile : The txt file containing the names of the restriction enzymes and their restriction site.
    Examples of formatting: DdeI C^TGAG
    
    Returns
    -------
    cutDNA : The DNA after having been cut by the restriction enzymes entered, in list format
    cuttingenzymes : The enzymes that cut the DNA, in list format

    '''
    
    bestand = open (enzymfile)
    string = DNA
    cuttingenzymes = []
    read = True
    while read == True:
        line = bestand.readline().strip()
        if line != '':    
            enzym, seq = line.split()
            site = seq
            site = site.replace("^","")
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
    A function that removes elements found in both lists and return a list containing all unique values

    Parameters
    ----------
    a : List 1
    b : List 2
    Returns
    -------
    pile : A list containing only the unique values

    '''
    pile = a + b
    pile = list(dict.fromkeys(pile))
    aset = set(a)
    bset = set(b)
    duplicates = list(set(max(aset,bset)).intersection(min(aset,bset)))
    for element in duplicates:
        pile.remove(str(element))
    return pile
