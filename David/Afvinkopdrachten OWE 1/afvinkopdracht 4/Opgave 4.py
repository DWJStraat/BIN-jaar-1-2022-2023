# Iteratie opdracht
# Start script voor opgave over sikkelcel
# (c) Martijn van der Bruggen, 2007-2010
# Updates:
# November 2010, code bijgewerkt met instructies voor de opdracht
# Hogeschool van Arnhem en Nijmegen

# Sequenties voor respectievelijk sikkelcel- en normale cellen
# Bekend is dat het gen coderend voor hemoglobine bij sikkelcel aandoening een andere nucleotide heeft
# De sequentie voor de sikkelcel en een "gezonde bloedcel" zijn hier onder gegeven
sikkel_seq = 'GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'
normaal_seq ='GAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCT'

# In het bestand enzymen. txt staan kandidaat restrictie enzymen
# Opdracht schrijf een programma dat al deze enzymen doorloopt een suggestie
# geeft welk restrictie enzym welk knipt in de ene sequentie en niet in de andere sequentie
# Hiermee kunnen we diagnostisch enzym voorstellen om vast te stellen of een persoon
# drager is van het sikkelcel allel
bestand = open ("enzymen.txt")


# Aanwijzingen voor het schrijven van je programma
# -------------------------------------------------------------
# Het lezen van een regel kan met bestand.readline() bijvoorbeeld: regel = bestand.readline(). Print de regel en bekijk wat hieruit komt
# Lees door totdat je een lege regel aantreft
# Een regel bestaat uit twee stukken enzym en knipsequentie. Bijvoorbeeld: DdeI C^TGAG
# Het opsplitsen van een regel in twee stukken op de spatie kan middels: enzym, seq = regel.split()
# Door bovenstaande split verkrijg je twee variabelen enzym en seq, respectievelijk de naam van het enzym en de sequentie waar deze in knipt
# Verwijderen het dakje uit de seq met seq.replace("^","")
# --------------------------------------------------------------------

# Auteur: David Straat
# Datum: 21 - sept - 2022
# Functie: 

    
def cutter(DNA, enzymfile):
    '''
    A function that can be used to process restriction enzymes found in a txt file on a string of DNA

    Parameters
    ----------
    DNA : The string of DNA to be analyzed
    enzymfile : The txt file containing the names of the restriction enzymes and their restriction site.
    Examples of formatting: DdeI C^TGAG
    
    Returns
    -------
    cutDNA : The DNA after having been cut by the restriction enzymes entered
    cuttingenzymes : The enzymes that cut the DNA

    '''
    
    bestand = open (enzymfile)
    string = DNA
    cuttingenzymes = []
    read = True
    while read == True:
        line = bestand.readline().strip()
        if line != '':    
            enzym, seq = line.split()
            site = seq
            site = site.replace("^","")
            sites = DNA.count(site)
            if sites > 0:
                string = string.replace(site, seq)
                cuttingenzymes.append(enzym)
        else:
            read = False
    cutDNA = string.split("^")
    return cutDNA, cuttingenzymes


sikkel_cut, sikkelenzyme = cutter(sikkel_seq, "enzymen.txt")
print(f'De volgende enzymen knippen in de sikkelcel sequentie:\n {sikkelenzyme}\nDe geknipte DNA string ziet er zo uit:\n{sikkel_cut}')
print('\n', '-'*50,'\n')
normaal_cut, normaalenzyme = cutter(normaal_seq, "enzymen.txt")            
print(f'De volgende enzymen knippen in de normale sequentie:\n {normaalenzyme}\nDe geknipte DNA string ziet er zo uit:\n{normaal_cut}')    

# Removes all enzymes that cut both DNA strings
enzymen = sikkelenzyme + normaalenzyme
enzymen = list(dict.fromkeys(enzymen))
sikkel = set(sikkelenzyme)
normaal = set(normaalenzyme)
duplos = list(set(max(sikkel,normaal)).intersection(min(sikkel,normaal)))
for element in duplos:
    enzymen.remove(str(element))
    
print('\n', '-'*50,'\n')
print(f'De volgende enzymen kunnen worden gebruikt om sikkelcel anemie te identificeren:\n{enzymen}')