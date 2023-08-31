# Naam: David straat
# Datum: 29 -sept -2022
# Versie: 4

# Voel je vrij om de variabelen/functies andere namen te geven als je 
# die logischer vind.


def lees_inhoud(bestands_naam):
    """
    This function takes a file and outputs the header and the sequence in
    separate format.

    Parameters
    ----------
    bestands_naam : The FASTA file to be examined in string format

    Returns
    -------
    header : The header of the FASTA
    seq: The sequence in the FASTA
    """
    header = ''
    seq = ''
    # Opens the file
    with open(bestands_naam, 'r') as file:
        for line in file:
            line = line.strip()
            if line[0] == '>':
                header = line
            else:
                seq += line

    return header, seq


def is_dna(seq):
    """
    This function checks if a sequence is DNA
    Parameters
    ----------
    seq : string

    Returns
    -------
    bool
    """
    allowed = set('A' + 'C' + 'T' + 'G')
    return set(seq) <= allowed


def knipt(seq, DNA):
    """
    This function takes a DNA sequence and a restriction enzyme site and
    Parameters
    ----------
    seq : string
    DNA : string

    Returns
    -------

    """
    site = seq
    site = site.replace("^", "")
    sites = DNA.count(site)
    if sites > 0:
        DNA = DNA.replace(site, seq)
    return DNA, sites


def main():
    """
    Asks for a file and a restriction enzyme site and returns the number of
    """
    bestand = "lamaseq.fasta"
    site = input('Enter the site where the enzyme cuts (example: ATT^TTA)\n')
    headers, seqs = lees_inhoud(bestand)
    if is_dna(seqs):
        DNAknip, sites = knipt(site, seqs)
        print(
            f'The DNA with the header:\n"{headers}"\ncontains {sites} '
            f'restriction enzyme sites')
    else:
        print('The FNA provided does not contain DNA')
    # schrijf hier de rest van de code nodig om de aanroepen te doen


main()
