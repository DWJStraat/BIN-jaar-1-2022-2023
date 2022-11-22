# importeer de twee dictionaries vanuit de translation.py
from translation import code


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
    protein_list = []
    starts = dna.count('ATG')
    while starts > 0:
        prot = ''
        start = dna.find('ATG')
        temporary_dna = dna[start:]
        while True:
            try:
                codon = temporary_dna[0:3].lower()
                if code[codon] == '*':
                    if prot != '':
                        protein_list.append(prot)
                    break
                prot += code[codon]
                temporary_dna = temporary_dna[3:]
            except KeyError:
                break
        dna = dna[start + 3:]
        starts -= 1

    return protein_list


def main(opdracht):
    """
    Deze functie vertaald een DNA-sequentie naar een eiwit sequentie

    Parameters
    ----------
    opdracht : int
        welke opdracht moet worden uitgevoerd. Keuze uit 2 en 3
    """
    dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTC" \
          "TTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG "
    complementary_dna = "TCGGTACATCGATTGAGTCCAATGTACCCCTACTGGGGCGCTG" \
                        "AACCTAATCTCAGAGAAAACCTTATTCGGACTTACTAGGCTCA" \
                        "TCGTAGAGTC "
    complementary_dna = complementary_dna[:: -1]
    if opdracht == 2:
        print(Opdracht2(dna))
    elif opdracht == 3:
        print(f'Forward:{Opdracht3(dna)}')
        print(f'Reverse:{Opdracht3(complementary_dna)}')
    else:
        print("Geen geldige opdracht gekozen")


main(3)
