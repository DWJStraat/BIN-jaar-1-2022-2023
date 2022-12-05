import re


class DNA():
    def __init__(self, sequence):
        self.sequence = sequence

    def setDNA(self, sequence):
        x = re.search('^[AGCTN]*$', sequence)
        if x:
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


a = DNA('AAA')

a.setDNA('AAAA')

print(a.getDNA())

