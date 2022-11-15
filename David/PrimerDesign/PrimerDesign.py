
import ../HORUS.py

fullDNA = HORUS.read.fna('gene.fna')

CodingDNA = HORUS.read.fna('coding.fna')

intronDNA = fullDNA.replace(CodingDNA, '|')

print(intronDNA)