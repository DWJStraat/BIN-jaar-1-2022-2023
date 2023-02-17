# Author: David Straat
# Date: 2022-feb-8
# Description : De class voor week 2

from textwrap import wrap
import numpy as np
import matplotlib.pyplot as plt


def calcGCsingle(sequence):
    GC = sequence.count("G") + sequence.count("C")
    AT = sequence.count("A") + sequence.count("T")
    return GC / (GC + AT)


def calcACGTsingle(sequence):
    ACGT = sequence.count("A") + sequence.count("C") + sequence.count(
        "G") + sequence.count("T")
    return ACGT / len(sequence)


class main:
    def __init__(self, filename, step=100):
        self.file = filename
        self.file_name = filename.split("\\")[-1]
        self.content = self.load_file()
        self.header = self.content[0]
        self.accession = self.header.split(" ")[0][1:]
        self.type = self.identify()
        self.code = self.process()
        self.gc = self.calcGC()
        self.n = self.gc
        self.length = len(self.code)
        self.step = step
        if self.type == "complete":
            self.gc_step = self.calcGCstep(self.step)
            self.gc_mean = np.mean(self.gc_step)
            self.gc_median = np.median(self.gc_step)
            self.gc_var = np.var(self.gc_step)*10000
            self.gc_std = np.std(self.gc_step)

    def load_file(self):
        with open(self.file, "r") as f:
            return f.readlines()

    def identify(self):
        headers = sum(1 for line in self.content if line.startswith(">"))
        if headers > 1:
            return "coding"
        elif headers == 1:
            contents = "".join(self.content[1:]).replace("\n", "")
            return "complete" if set(contents) <= set("ATGCNMR") else "prot"
        else:
            return "invalid"

    def process(self):
        if self.type == "complete":
            return ''.join(self.content[1:]).replace("\n", "")
        elif self.type == "coding":
            return self.process_coding()
        else:
            return "invalid"

    def process_coding(self):
        first_line = True
        entry = ['', '']
        contents = []
        for line in self.content:
            if line.startswith(">"):
                entry = ['', '']
                if first_line:
                    first_line = False
                else:
                    contents.append(entry)
                entry[0] = line
            else:
                entry[1] += line
        return contents

    def calcGC(self):
        if self.type == "complete":
            return calcGCsingle(self.code)
        elif self.type == "coding":
            # return self.calcGCcoding()
            return {i[0]: calcGCsingle(i[1]) for i in self.code}

    def calcGCstep(self, step):
        step_code = wrap(self.code, step)
        return [calcGCsingle(step_code[i]) for i in range(len(step_code))]

    def calcACGT(self):
        if self.type == "complete":
            return calcACGTsingle(self.code)
        elif self.type == "coding":
            return {i[0]: calcACGTsingle(i[1]) for i in self.code}

    def calcACGTstep(self, step):
        step_code = wrap(self.code, step)
        return [calcACGTsingle(step_code[i]) for i in
                range(len(step_code))]

    def estimateGC(self, step):
        if self.type == "complete":
            AGCT = self.calcACGTstep(step)
            unknown_percentage = [1 - AGCT[i] for i in range(len(AGCT))]
            length = len(self.code)
            unknown = np.mean(unknown_percentage) * length
            unknown_gc = unknown * self.gc
            return unknown_gc / length

    def plotGC(self):
        unknown_val = self.estimateGC(self.step)
        steps = self.gc_step
        estimate = steps + [unknown_val]
        for i in range(len(steps)):
            steps[i] = steps[i] * 100
        for i in range(len(estimate)):
            estimate[i] = estimate[i] * 100
            if estimate[i] == 0:
                estimate[i] = None
        f, ax = plt.subplots()
        ax.set_xlim(0, len(self.code)/self.step)
        ax.set_ylim(0, 100)
        plt.plot(estimate, color="red")
        plt.plot(steps, color="blue")

        plt.xlabel(f"{self.step} bp")
        plt.ylabel("Percentage of DNA in %")
        plt.title(f"GC content of {self.accession}")
        plt.legend(["Estimated GC", "GC"])

        return plt