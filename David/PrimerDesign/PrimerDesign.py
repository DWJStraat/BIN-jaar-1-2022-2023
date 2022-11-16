import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import HORUS

fullDNA = HORUS.read.fna('gene.fna')

CodingDNA = HORUS.read.fna('coding.fna')
temperature = {'A': 2, 'T': 2, 'G': 4, 'C': 4}
reverse = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
mintemp = 50
maxtemp = 60
targetsize = 20
intronDNA = fullDNA.replace(CodingDNA, '\n')

intronDNA = intronDNA.split('\n')

print(intronDNA)
intronDNA[0] = intronDNA[0][::-1]

primertemp1 = 0
counter1 = 0
primer1 = ''
for i in intronDNA[0]:
    primertemp1 += temperature[i]
    primer1 += reverse[i]
    counter1 += 1
    if counter1 < 20 and primertemp1 < 60:
        continue
    elif counter1 > 20 and 60 > primertemp1 > 50 or primertemp1 > 60:
        break
print(f'Primer 1 temperature:{primertemp1}Celcius')
print(f"Primer 1: 5' {primer1[::-1]} 3'")
print(f'Primer 1 Length: {len(primer1)}')

primertemp2 = 0
counter2 = 0
primer2 = ''
for i in intronDNA[1]:
    primertemp2 += temperature[i]
    primer2 += reverse[i]
    counter2 += 1
    if counter2 > targetsize and primertemp2 < mintemp:
        continue
    if mintemp < primertemp2 < maxtemp:
        break
print(f'Primer 2 temperature:{primertemp2} Celcius')
print(f"Primer 2: 5' {primer2} 3'")
print(f'Primer 2 Length: {len(primer2)}')