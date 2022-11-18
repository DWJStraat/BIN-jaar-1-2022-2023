# importeer de twee dictionaries vanuit de translation.py
from translation import code
from translation import aa3


def Opdracht2(dna):
    """
    Deze functie vertaalt een DNA sequentie naar een eiwit sequentie

    Parameters
    ----------
    dna : string
        DNA sequentie

    Returns
    -------
    eiwit : string
        eiwit sequentie
    """
    prot = ''
    for i in range(0, len(dna), 3):
        try:
            codon = dna[i:i + 3].lower()
            prot += code[codon]
        except KeyError:
            break
    return prot


def Opdracht3(dna):
    """
    Deze functie vertaalt een DNA sequentie naar een eiwit sequentie

    Parameters
    ----------
    dna : string
        DNA sequentie

    Returns
    -------
    eiwit : string
        eiwit sequentie
    """
    run = True
    prot = ''
    dna = dna.lower()
    start = dna.count('atg')
    while run == True:
        while start > 0:
            startpost = dna.find('atg')
            post = startpost
            while post < len(dna):
                codon = dna[post:post + 3]
                try:
                    if code[codon] == '*':
                        start = start -1
                        stoppos = post + 3
                        prot += '\t'
                        dna = dna[stoppos:]
                        break
                except KeyError:
                    run = False
                else:
                    try:
                        prot += code[codon]
                        post += 3
                    except KeyError:
                        break
    return prot


def main(opdracht):
    """
    Deze functie vertaald een DNA sequentie naar een eiwit sequentie

    Parameters
    ----------
    opdracht : int
        welke opdracht moet worden uitgevoerd. Keuze uit 2 en 3
    """
    dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAA\
    TAAGCCTGAATGATCCGAGTAGCATCTCAG"
    if opdracht == 2:
        print(Opdracht2(dna))
    elif opdracht == 3:
        print(Opdracht3(dna))
    else:
        print("Geen geldige opdracht gekozen")


main(3)
