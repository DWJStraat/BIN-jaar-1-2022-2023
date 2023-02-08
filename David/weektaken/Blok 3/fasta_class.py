import statistics
from textwrap import wrap

import matplotlib.pyplot as plt


class Fasta:
    def __init__(self, file, file_type="fasta", fasta_name=None):
        self.GC_percent = None
        self.GC_mean = None
        self.GC_median = None
        self.GC_stdev = None
        self.GC_average = None
        self.file_type = file_type
        self.file = file
        self.type = self.identify()
        self.content = None
        self.fasta_name = fasta_name

    def loadFile(self, content):
        if self.file_type == "fasta":
            self.loadFasta(content)
        else:
            print("Invalid filetype")

    def loadFasta(self, content):
        file_contents = self.read()
        if content in ["complete", "prot"]:
            contents = "".join(file_contents[1:])
        elif content == "coding":
            first_line = True
            entry = ['', '']
            contents = []
            for line in file_contents:
                if line.startswith(">"):
                    entry = ['', '']
                    if first_line:
                        first_line = False
                    else:
                        contents.append(entry)
                    entry[0] = line
                else:
                    entry[1] += line
        self.content = contents

    def identify(self):
        file_content_list = self.read()
        headers = 0
        for i in file_content_list:
            if i == "":
                file_content_list.remove(i)
            elif i[0] == ">":
                headers += 1
        if headers > 1:
            return "coding"
        elif headers == 1:
            contents = "".join(file_content_list[1:])
            return "complete" if set(contents) <= set("ATGC") else "prot"
        else:
            return "invalid"

    def read(self):
        contents = []
        with open(self.file, "r") as f:
            contents.extend(line.strip() for line in f)
        return contents

    def calcGC(self):
        print(self.type)
        sequence = self.content
        if self.type == "complete":
            GC_percent = self.calcGCsingle(sequence)
            self.GC_percent = GC_percent
            return GC_percent
        elif self.type == "coding":
            GC_percent = {}

            for i in sequence:
                if i is None:
                    break
                percent = self.calcGCsingle(i[1])

                GC_percent[i[0]] = percent
            self.GC_percent = GC_percent
            self.GC_mean = statistics.mean(GC_percent.values())
            self.GC_median = statistics.median(GC_percent.values())
            self.GC_stdev = statistics.stdev(GC_percent.values())
            self.GC_average = sum(GC_percent.values()) / len(
                GC_percent.values())
        elif self.type == "prot":
            print("Does no have a GC%")
            return
        else:
            print("Invalid content")
            return

    def calcGCsingle(self, sequence):
        try:
            AT = sequence.count("A") + sequence.count("T")
            GC = sequence.count("G") + sequence.count("C")
            total = AT + GC
            return GC / total
        except Exception:
            print("Invalid content")
            return

    def calcGCFraction(self, sequence=None, fraction=100):
        if sequence is None:
            sequence = self.content
        fraction_sequence = wrap(sequence, fraction)
        return [self.calcGCsingle(i) for i in fraction_sequence]

    def plotGC(self):
        if self.type == "complete":
            fractions = self.calcGCFraction()
            names = list(range(len(fractions)))
            values = fractions
            plt.plot(names, values)
            plt.title("GC% of the selected FASTA")
            plt.xlabel(f"Fraction of the selected sequence in steps of 100")
            plt.ylabel("GC% on a range of 1-0")
            return plt
        if self.type == "coding":
            fractions = self.GC_percent
            return fractions


a = Fasta(r"C:\Users\dstra\OneDrive - HAN\OWE 3\FASTAs\HIV1\HIV1_complete.fna")
a.loadFile('complete')
print(a.type)
a.calcGC()
print(a.GC_percent)
a.plotGC().show()

#
# b = Fasta(r"C:\Users\dstra\OneDrive - HAN\OWE 3\FASTAs\HIV1\HIV1_coding.fna")
# b.loadFile('coding')
# print(b.type)
# b.calcGC()
# print(b.GC_percent['total'])
# b.plotGC().show()
