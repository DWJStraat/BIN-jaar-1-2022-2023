import matplotlib.pyplot as plt

input_str = 'atgagccaaatacataaacatcctattccagctgcaattgcagagcatgctctaattacc'
class bias:
    def __init__(self, input_str):
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
        self.codon_bias = self.get_codon_bias()
        self.amino_acid_bias = self.get_amino_acid_bias()

    def get_codon_bias(self):
        bias = {}
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3]
            if codon in bias:
                bias[codon] += 1
            else:
                bias[codon] = 1
        return bias

    def get_amino_acid_bias(self):
        bias = {}
        amino_acids = []
        for amino_acid in self.codons.values():
            if amino_acid not in amino_acids:
                amino_acids.append(amino_acid)
        for codon in self.codon_bias:
            amino_acid = self.codons[codon]
            if amino_acid in bias:
                if codon in bias[amino_acid]:
                    bias[amino_acid][codon] += 1
                else:
                    bias[amino_acid][codon] = 1
            else:
                bias[amino_acid] = {codon: 1}
        return bias

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

a = bias(input_str)
a.plot_amino_acid("Ile")