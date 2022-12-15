import random
import matplotlib.pyplot as plt


def opdracht1(x, y, z):
    """
    Opdracht 1

    Maak een grafiek van de lijsten x, y en z.

    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    y : list
        Lijst met y-coordinaten
    z : list
        Lijst met z-coordinaten
    """
    scatter(x, y, 'Scatterplot')

    line(x, y, 'Lineplot')

    bar(x, y, 'Barplot')

    pie(x, y, 'Pieplot')

    bar(x, y, 'Barplot')

    scatterbar(x, y, z, 'Scatterplot en Barplot')

def opdracht2(bestand):
    patientdata = readcsv(bestand)
    pat_id = []
    med_a = []
    med_b = []
    doc = []
    for i in patientdata:
        pat_id.append(int(i[0]))
        med_a.append(int(i[1]))
        med_b.append(int(i[2]))
        doc.append(i[3])
    med_b_use = [0, 0, 0]
    for j in med_b:
        if j < 40:
            med_b_use[0] += 1
        elif 40 <= j <= 50:
            med_b_use[1] += 1
        elif j > 50:
            med_b_use[2] += 1

    scatter(med_a, med_b, 'Medicijn A tegenover Medicijn B')
    line(pat_id, med_a, 'Dosis Medicijn A per patient')
    histo(doc, 'Aantal patienten per arts')
    pie(med_b_use, ['<40', '40-50', '>50'], 'Gebruik van medicijn B')
    scatterbar(med_b, med_a, pat_id,
               'Medicijn B tegenover Medicijn A en patienten')

def opdracht3(bestand, european=False):
    """
    Maak een histogram van de lijst met waardes uit het csv bestand.

    Parameters
    ----------
    bestand : str
        Naam van het csv bestand
    european : bool
        True als het csv bestand een ; als scheidingsteken gebruikt
        Default is False
    """
    data = readcsv(bestand, european)
    waardes = []
    for i in data:
        try:
            waardes.append(i[1])
        except:
            continue
    fig, ax = plt.subplots()
    plt.hist(waardes, color='red', label=waardes)
    ax.title.set_text('Histogram')
    ax.set_xlabel('Status')
    ax.set_ylabel('Aantal genen')
    ax.legend()
    plt.show()

def readcsv(file_name, european=False):
    """
    Lees een csv bestand in en zet deze om naar een lijst van lijsten.

    Parameters
    ----------
    file_name : str
        Naam van het csv bestand
    european : bool
        True als het csv bestand een ; als scheidingsteken gebruikt
        Default is False
    Returns
    -------
    csv: list
        Lijst van lijsten met de data uit het csv bestand
    """
    teller = 0
    csv = []
    with open(file_name) as file:
        for ln in file:
            teller += 1
            ln = ln.replace("\n", "")
            if european:
                csvline = ln.split(';')
            else:
                csvline = ln.split(',')
            csv.append(csvline)
    del csv[0]
    if european:
        print('European mode enabled. Consider switching to , instead of ; as '
              'this is compliant with RFC 4180')
    return csv


def bar(x, y, title):
    """
    Maak een barplot van de lijsten x en y.

    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    y : list
        Lijst met y-coordinaten
    title : str
        Titel van de grafiek
    """
    fig, ax = plt.subplots()
    plt.bar(x, y, color='red', label=y)
    ax.title.set_text(title)
    plt.show()


def line(x, y, title):
    """
    Maak een lineplot van de lijsten x en y.

    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    y : list
        Lijst met y-coordinaten
    title : str
        Titel van de grafiek
    """
    fig, ax = plt.subplots()
    plt.plot(x, y, color='red', label=y)
    ax.title.set_text(title)
    plt.show()


def scatter(x, y, title):
    """
    Maak een scatterplot van de lijsten x en y.

    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    y : list
        Lijst met y-coordinaten
    title : str
        Titel van de grafiek
    """
    fig, ax = plt.subplots()
    plt.scatter(x, y, color='red', label=y)
    ax.title.set_text(title)
    plt.show()


def pie(x, y, title):
    """
    Maak een pieplot van de lijsten x en y.

    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    y : list
        Lijst met y-coordinaten
    title : str
        Titel van de grafiek
    """
    fig, ax = plt.subplots()
    plt.pie(x, labels=y)
    ax.title.set_text(title)
    plt.show()


def scatterbar(x, y, z, title):
    """
    Maak een scatterplot en barplot van de lijsten x, y en z.
    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    y : list
        Lijst met y-coordinaten
    z : list
        Lijst met z-coordinaten
    title : str
        Titel van de grafiek
    """
    fig, ax = plt.subplots()
    plt.bar(x, z, color='blue', label='z')
    plt.scatter(x, y, color='red', label='y')
    ax.title.set_text(title)
    plt.show()


def histo(x, title):
    """
    Maak een histogram van de lijst x.

    Parameters
    ----------
    x : list
        Lijst met x-coordinaten
    title : str
        Titel van de grafiek
    """
    fig, ax = plt.subplots()
    plt.hist(x, color='red', label=x)
    ax.title.set_text(title)
    plt.show()


def main():
    ### OPDRACHT 1 ###
    # Gebruik de lijsten x y en z voor de grafieken van opdracht 1
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 6, 8, 10, 12, 12, 4, 14, 7, 10]
    z = []
    for i in range(0, 10):
        n = random.randint(1, 100)
        z.append(n)

    opdracht1(x, y, z)

    ### OPDRACHT 2 ###
    # Bestand voor opdracht 2
    patienten = "patienten.csv"
    opdracht2(patienten)

    ### OPDRACHT 3 ###
    # Bestand voor opdracht 3
    gist = "yeast_genes.csv"
    opdracht3(gist)

    ### OPDRACHT 4 ###
    # Bestand voor opdracht 4
    test = "test.csv"
    opdracht3(test, True)

main()
