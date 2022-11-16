import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import HORUS

fullDNA = HORUS.read.fna('gene.fna')

CodingDNA = HORUS.read.fna('coding.fna')


a1, a2, b1, b2 = HORUS.primerDesign(fullDNA, CodingDNA)
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
