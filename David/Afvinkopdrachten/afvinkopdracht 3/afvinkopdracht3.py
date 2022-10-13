#################################################################################
# Controle op enzymen die knippen in een sequentie
# Bron GenBank bestand: http://www.canr.msu.edu/lgc/GenBankfiles/AF165912.htm
# Auteur: Martijn van der Bruggen
#         HAN University
# Creatie: november 2008 (MvdB)
# Updates:
# november 2009, aanpassing aan nieuw boek (MvdB)
# november 2010, Dictionary met enzymen en knipplaats opgeheven (MvdB)
# november 2011, aanpassing syntax voor Python3 compatibility door Stephan Heijl
# november 2011, leesbaarheid functie aangepast (MvdB) 
# november 2014, aanpassing aan nieuw boek (EK) en extra commentaar
# oktober 2021, aanpassing met extra commentaar (TP)
# september 2022, missende delen ingevoegd door David Straat
#################################################################################

# Enzymen met knipprofiel
# Voor meer informatie over restrictie enzymen bekijk: http://nl.wikipedia.org/wiki/Restrictie-enzym
# Lijst met restrictie enzymen, sequentie waar ze in knippen en het organisme waar ze in voorkomen
DdeI   = "CTGAG"    #knipt op C^TGAG      Desulfovibrio desulfuricans    	
BspMII = "TCCGGA"   #knipt op T^CCGGA     Klebsiella pneumoniae 
EcoRI  = "GAATTC"   #knipt op G^AATTC     Escherichia coli
HindIII= "AAGCTT"   #knipt op A^AGCTT     Haemophilus influenzae
TaqI   = "TCGA"     #knipt op T^CGA    	  Thermus aquaticus

# Lees een bestand en parse de sequentie
def getSequentie (bestandsnaam):
    """Haal de sequentie uit het bestand

    Input:
    bestandsnaam - string, naam van het bestand met de sequentie

    Output:
    sequence - string, sequentie 
    """
    bestand = open (bestandsnaam,encoding="latin1")
    startReading = False            #Zolang die false is niets toevoegen aan sequentie
    raw_data = ""   
    for regel in bestand:
        if startReading:            # Hier staat hetzelfde als 'if startReading == True'. 
                                    # De if statement moet een True opleveren om te kunnen plaatsvinden.
                                    # startReading is een bool, dus pas als deze True is, kan de if een True opleveren.
            raw_data += regel[10:]  # lees van iedere regel alleen het DNA
        if "ORIGIN" in regel:
            startReading = True     # Startpunt van DNA sequentie gevonden
    #Verwijder uit de sequentie alle spaties, next line tokens
    sequence= raw_data.replace(' ','').replace('\n','').replace('\r','')
    return sequence                 # retourneer een sequentie zonder extra chars

def snip(string, site):
    # Verandert de string naar uppercase
    string = string.upper()
    # Telt hoevaak de knip site voorkomt op de sequentie
    i = string.count(site)
    # Lege variabelen
    start = 0
    snips = []
    output = ''
    nextstart = 0
    # Als er tenminste 1 site aanwezig is, scant de While loop de sequentie, returned 
    # de locaties van de sites, en stopt een ^ op de plaats van de cut.
    if i > 0:
        while i > 0 :
            snip = string.find(site, nextstart)
            output = string[start:snip] + '^'
            snips.append(snip)
            i = i - 1
            nextstart = snip +1
        output = output + string[snip:]
    else:
    # Als er geen site aanwezig is, output de functie dezelfde string
        output = string
    

    return output, snips 

# Doorzoek nu de sequentie op knipplaatsen.
# Toon voor ieder enzym uit de dictionary of deze knipt of niet.
# In de uitvoer staat bijvoorbeeld:
# >>> BamH1 knipt wel
# >>> EcoRII knipt niet
# (Optioneel) Toon de ontstane fragmenten voor iedere knip

# Bonus: geef per enzym aan op welke posities van het DNA er geknipt is
# De uitvoer wordt dan bijvoorbeeld:
# >>> BamH1 knipt op positie 57
# >>> EcoRII knipt niet

def main():
    # De sequentie wordt opgehaald
    sequentie = getSequentie("startOpgave3.txt")

    print ("De sequentie waar de enzymen in kunnen knippen")
    print ("-"*80)
    print (sequentie)
    print ("-"*80)
    
    # Schrijf hier de code om te checken of deze enzymen knippen in de sequentie
    print ("Enzymen die onderzocht worden:")
    print ("DdeI ", DdeI)
    print ("BspMII ", BspMII)
    print ("EcoRI ", EcoRI)
    print ("HindIII ", HindIII)
    print ("TaqI ", TaqI)
    print ("-"*80)
    # Gaat elk enzym langs, plaats een ^ op de knip site, en output de resultaten en
    # de locaties.
    a1, a2 = snip(sequentie, DdeI)
    print(f"DdeI knipt op de posities {a2}")
    b1, b2 = snip(a1, BspMII)
    print(f'BspMII knip op de posities {b2}')
    c1, c2 = snip(b1, EcoRI)
    print(f'EcoRI knipt op de posities {c2}')
    d1, d2 = snip(c1, HindIII)
    print(f'HindIII knipt op de posties {d2}')
    e1, e2 = snip(d1, TaqI)
    print(f'TaqI knipt op de posities {e2}')

    # Knipt de string op op de knip plekken, en maakt er een lijst van
    result = e1.split("^")
    print(f"De sequentie is geknipt tot de volgende genen: {result}")

main()
