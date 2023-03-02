import matplotlib.pyplot as plt
import numpy as np


class bias:
    def __init__(self, input_str, name = None):
        self.codons = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
          "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
          "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
          "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
          "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
          "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
          "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
          "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
          "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
          "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
          "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
          "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
          "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
          "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
          "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
          "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
          }
        self.sequence = input_str.upper().replace('T', 'U')
        self.name = name
        self.codon_bias = None
        self.amino_acid_bias = None
        self.total = len(self.sequence) / 3

    def get_codon_bias(self):
        bias = {}
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3]
            if codon in bias:
                bias[codon] += 1
            else:
                bias[codon] = 1
        return bias

    def set_codon_bias(self):
        self.codon_bias = self.get_codon_bias()

    def get_amino_acid_bias(self):
        bias = {}
        amino_acids = []
        for amino_acid in self.codons.values():
            if amino_acid not in amino_acids:
                amino_acids.append(amino_acid)
        for codon in self.codon_bias:
            amino_acid = self.codons[codon]
            if amino_acid in bias:
                bias[amino_acid][codon] = self.codon_bias[codon]
            else:
                bias[amino_acid] = {codon: 1}
        return bias

    def set_amino_acid_bias(self):
        self.amino_acid_bias = self.get_amino_acid_bias()

    def plot_amino_acid(self, amino_acid):
        if amino_acid in self.codons.values():
            dictionary = self.amino_acid_bias[amino_acid]
            names = dictionary.keys()
            values = dictionary.values()
            plt.pie(values, labels = names, autopct='%1.1f%%', shadow=True, startangle=90)
            plt.title(f"Frequency of codons for {amino_acid}")
            plt.show()
        else:
            print("Amino acid not found")


    def plot_organism(self):
        dictionary = self.codon_bias
        dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
        dictionary = dict(reversed(list(dictionary.items())))
        names = list(dictionary.keys())
        values = list(dictionary.values())
        colors = []
        color = iter(plt.cm.rainbow(np.linspace(1, 0, len(names))))
        for i in range(len(names)):
            try:
                c = next(color)
                colors.append(c)
            except StopIteration:
                colors.append('')
        explode = []
        for i in range(len(names)):
            explode.append(0.1)
        plt.rcParams['font.size'] = 8.0
        plt.rcParams['figure.figsize'] = 10,10
        plt.pie(values, colors = colors, shadow=True, startangle=90,
                explode= explode, counterclock=False)
        plt.title(f"Frequency of codons for the genome of the {self.name}")
        plt.legend(loc="best",
                   labels = [f"{names[i]}: {values[i]/self.total*100:.2f}%" for i in range(len(names))],
                   bbox_to_anchor=(0.15, 0.15, -0.15, 1)
                   )
        my_circle = plt.Circle((0, 0), 0.8, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.show()