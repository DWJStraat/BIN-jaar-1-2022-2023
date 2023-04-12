import regex as re
from Bio.Seq import Seq

protein_to_codon = {
    "A": "GCT", "C": "TGT", "D": "GAT", "E": "GAA",
    "F": "TTT", "G": "GGT", "H": "CAT", "I": "ATT",
    "K": "AAA", "L": "TTA", "M": "ATG", "N": "AAT",
    "P": "CCT", "Q": "CAA", "R": "CGT", "S": "TCT",
    "T": "ACT", "V": "GTT", "W": "TGG", "Y": "TAT",
    "STOP": "TAA", "*":"TAA"
}

def sequence_identifier(sequence):
    DNA = re.search(r"^[ATGC]+$", sequence)
    RNA = re.search(r"^[AUGC]+$", sequence)
    Protein = re.search(r"^[ARNDCQEGHILKMFPSTWYV]+$", sequence)
    if DNA:
        output = list(DNA_handle(sequence))
        type = "DNA"
    elif RNA:
        output = list(RNA_handle(sequence))
        type = "RNA"
    elif Protein:
        output = list(Protein_handle(sequence))
        type = "Protein"
    else:
        return "Invalid sequence"
    for i in output:
        output[output.index(i)] = str(i)
    return {
        "DNA": output[0],
        "RNA": output[1],
        "Protein": output[2],
        "Type": f'The sequence entered is {type}'
    }

def DNA_handle(sequence):
    DNA = Seq(sequence)
    RNA = f'RNA: {DNA.transcribe()}'
    DNA_length = len(DNA)
    DNA = DNA[:-DNA_length//3]
    Protein = f'Protein: {DNA.translate()}'
    DNA = ''
    return DNA, RNA, Protein


def RNA_handle(sequence):
    RNA = Seq(sequence)
    DNA = f'DNA: {RNA.back_transcribe()}'
    Protein = f'Protein: {RNA.translate()}'
    RNA = ''
    return DNA, RNA, Protein

def Protein_handle(sequence):
    Protein = Seq(sequence)
    RNA = Seq("".join(protein_to_codon[aminoacid] for aminoacid in Protein))
    DNA = RNA.back_transcribe()
    RNA = f'RNA: {RNA}'
    DNA = f'DNA: {DNA}'
    Protein = ''
    return DNA, RNA, Protein
