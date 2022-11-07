# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:32:23 2022

@author: dstra
"""


def lees_inhoud(file_name='enzymen.txt'):
    bestand = open(file_name)
    enzymenlijst = [[], []]
    read = True
    while read == True:
        line = bestand.readline().strip()
        if line != '':
            enzym, seq = line.split()
            enzymenlijst[0].append(enzym)
            enzymenlijst[1].append(seq)
        else:
            read = False
    return enzymenlijst


def match(sequentie, enzymenlijst):
    knippen = []
    cutDNA = []
    for i in range(0, len(enzymenlijst[0])):
        naam = enzymenlijst[0][i]
        enzym = enzymenlijst[1][i]
        code = enzym.replace("^", "")
        knip = sequentie.count(code)
        if knip > 0:
            sequentie = sequentie.replace(code, enzym)
            knippen.append(enzym)
            knip_locaties = [i for i, letter in enumerate(
                sequentie) if letter == '^']
            print(
                f'match met {naam} op de locaties {knip_locaties}.')
    cutDNA = sequentie.split("^")
    DNA = ', '.join(cutDNA)
    print(DNA)


def main():
    enzymenlijst = lees_inhoud()
    sequentie = 'ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC'
    match(sequentie, enzymenlijst)


main()
