"""
Overgeschreven van Thijn van Kempen tijdens de nabespreking van de toets op 18 Oktoboer 2022 door David Straat
"""
def aantal_a_t_mutaties(bestandsnaam):
    a_t_teller = 0
    try:
        with open(bestandsnaam) as geopend_bestand:
            sla_over = geopend_bestand.readline()
            for regel in geopend_bestand:
                regel = regel.replace("\n", "")
                regel = regel.split("\t")
            try:
                referentie = regel[3]
                alternatief = regel[4]
                if referentie == "A" and alternatief == "T":
                    a_t_teller += 1
            except ValueError:
                print("Waardes niet correct")
    except FileNotFoundError:
        print('Bestand is niet gevonden')
    except:
        print("Onbekende fout")
    return a_t_teller


def quality_lager_dan(bestandsnaam, quality=35):
    """
    Print alle mutaties onde bepaalde quality score.
    :param bestandsnaam: Naam en path van .vcf file
    :param quality: Kwaliteitsscore. Default 35.
    :return: None
    """
    quality_teller = 0
    try:
        with open(bestandsnaam) as geopend_bestand:
            sla_over = geopend_bestand.readline()
            for regel in geopend_bestand:
                regel = regel.replace("\n", "")
                regel = regel.split("\t")
                try:
                    quality_kolom = int(regel[5])
                    if quality_kolom < quality:
                        # print(regel)
                        quality_teller += 1
                except ValueError:
                    print("Kwaliteitskolom is geen integere waarde.")
        print(quality_teller)

    except FileNotFoundError:
        print('Bestand is niet gevonden')
    except:
        print("Onbekende fout, neem contact op met de maker van de applicatie.")


def unieke_filters(bestandsnaam):
    """
    Zoekt naar alle filter methodes en slaat elk type 1x op
    :param bestandsnaam
    :return: unieke_waarden: alle unieke filters
    """
    filters = []
    try:
        with open(bestandsnaam) as geopend_bestand:
            sla_over = geopend_bestand.readline()
            for regel in geopend_bestand:
                regel = regel.replace("\n", "")
                regel = regel.split("\t")
                try:
                    filter_kolom = regel[6]
                    if filter not in filters:
                        filters.append(filter_kolom)
                except IndexError:
                    print(
                        "Kolom waarde niet gevonden. Mogelijk is de layout niet uniform.")
        return filters

    except FileNotFoundError:
        print('Bestand is niet gevonden')
    except:
        print('Onbekende fout, neem contact op met de maker van de applicatie.')


if __name__ == "__main__":
    """
    De main functie waarin we verschillende functies aanroepen van dit script.
    """
    aantal_a_t = aantal_a_t_mutaties('chr1.vcf')
    quality_Vraag = input(
        'Wilt u de default quality (35) filter toepassen? \nType Ja om dit in te stellen')
    if quality_Vraag == 'Ja':
        quality = input('Geef een quality waarde in')
        quality_lager_dan('chr1.vcf')
    else:
        quality_limiet = int(
            input("Tot welke quality scores wilt u de mutaties weergeven?"))
        quality_lager_dan('chr1.vcf', quality_limiet)
    filters = unieke_filters('chr1.vcf')
