import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import HORUS

fullDNA = HORUS.read.fna('gene.fna')

CodingDNA = HORUS.read.fna('coding.fna')


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


a1, a2, b1, b2 = primerDesign(fullDNA, CodingDNA)
print('Forward Primer')
print('--------------')
print(f'Temperature:{b1} Celcius')
print(f"Sequence: 5' {a1} 3'")
print(f'Length: {len(a1)}')
print('\n')
print('Reverse Primer')
print('--------------')
print(f'Temperature:{b2} Celcius')
print(f"Sequence: 5' {a2} 3'")
print(f'Length: {len(a2)}')
