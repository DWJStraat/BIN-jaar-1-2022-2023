import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import HORUS

fullDNA = HORUS.Read.fna('gene.fna')

CodingDNA = HORUS.Read.fna('coding.fna')

a1, a2, b1, b2 = HORUS.primerDesign(fullDNA, CodingDNA, maxtemprange=2,
                                    minsize=18, maxtemp=62)
print('Forward Primer')
print('--------------')
print(f'Temperature:{b1} Celsius')
print(f"Sequence: 5' {a1} 3'")
print(f'Length: {len(a1)}')
print('\n')
print('Reverse Primer')
print('--------------')
print(f'Temperature:{b2} Celsius')
print(f"Sequence: 5' {a2} 3'")
print(f'Length: {len(a2)}')
