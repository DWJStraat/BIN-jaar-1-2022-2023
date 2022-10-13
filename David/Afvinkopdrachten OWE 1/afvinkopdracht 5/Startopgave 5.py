# Naam: David straat
# Datum: 29 -sept -2022
# Versie: 4

# Voel je vrij om de variabelen/functies andere namen te geven als je 
# die logischer vind.

  
    
def lees_inhoud(bestands_naam):
    '''
    This function takes a file and outputs the header and the sequence in separate format.
    
    Parameters
    ----------
    file : The FASTA file to be examined in string format
    
    Returns
    -------
    header : The header of the FASTA
    seq: The sequence in the FASTA
    '''
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
    allowed = set('A'+'C'+'T'+'G')
    if set(seq) <= allowed :
        DNA = True
    else:
        DNA = False
    return DNA
    

def knipt(seq,DNA):
    site = seq
    site = site.replace("^","")
    sites = DNA.count(site)
    if sites > 0:
        DNA = DNA.replace(site, seq)
    return DNA, sites


def main():

    bestand = "lamaseq.fasta" 
    site = input('Enter the site where the enzyme cuts (example: ATT^TTA)\n')
    headers, seqs = lees_inhoud(bestand) 
    DNA = is_dna(seqs)
    if DNA:
        DNAknip, sites = knipt(site, seqs)
        print(f'The DNA with the header:\n"{headers}"\ncontains {sites} restriction enzyme sites')
    else:
        print('The FNA provided does not contain DNA')
    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
main()
