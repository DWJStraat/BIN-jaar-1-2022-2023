import re

class fasta:

    def __init__(self):
        self.header = None
        self.sequence = None
        self.type = None

    def setHeader(self, header):
        if header.startswith('>') and header.isdigit():
            self.header = header
        else:
            print('Invalid header')

    def getHeader(self):
        return self.header

    def findType(self):
        if re.search('^[AGCTN]*$', self.sequence):
            self.type = 'DNA'
        elif re.search('^[AGCUN]*$', self.sequence):
            self.type = 'RNA'
        elif re.search('^[ACDEFGHIKLMNPQRSTVWY]*$', self.sequence):
            self.type = 'Protein'
        else:
            print('Invalid sequence')

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setSequence(self, sequence):
        if self.type == 'DNA':
            if re.search('^[AGCTN]*$', sequence):
                self.sequence = sequence
            else:
                print('Invalid DNA sequence')
        elif self.type == 'RNA':
            if re.search('^[AGCUN]*$', sequence):
                self.sequence = sequence
            else:
                print('Invalid RNA sequence')
        elif self.type == 'Protein':
            if re.search('^[ACDEFGHIKLMNPQRSTVWY]*$', sequence):
                self.sequence = sequence
            else:
                print('Invalid Protein sequence')

    def getSequence(self):
        return self.sequence

class DNA:

    def __init__(self):
        self.sequence = None

    def setDNA(self, sequence):
        self.sequence = sequence

    def getDNA(self):
        return self.sequence

    def getTranscript(self):
        transcript = ''
        for i in self.sequence:
            if i == 'T':
                transcript += 'U'
            else:
                transcript += i
        return transcript

    def getLength(self):
        return len(self.sequence)

    def getGcPercent(self):
        length = len(self.sequence)
        GC = self.sequence.count('G') + self.sequence.count('C')
        GCpercent = GC / length
        return GCpercent

