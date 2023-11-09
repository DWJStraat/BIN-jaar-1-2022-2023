"""
A script written by David Straat
"""

import random
import matplotlib.pyplot as plt


def opdracht_1(x, y, z):
    """
    Opdracht 1

    Generates a plot based on the lists X, Y, and Z

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

    scatterbar(x, y, z, 'Scatterplot and Barplot')


def opdracht_2(file):
    """
    Generates a scatterplot from data in the file provided
    Parameters
    ----------
    file
    """
    patient_data = read_csv(file)
    pat_id = []
    med_a = []
    med_b = []
    doc = []
    for i in patient_data:
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

    scatter(med_a, med_b, 'Medicine A vs Medicine B')
    line(pat_id, med_a, 'Dose Medicine A per patient')
    histo(doc, 'Patients per doctor')
    pie(med_b_use, ['<40', '40-50', '>50'], 'Usage of Medicine B')
    scatterbar(med_b, med_a, pat_id,
               'Medicine B vs Medicine A and patients')


def opdracht_3(file, european=False):
    """
    Makes a histogram out of a list of values from a CSV file.

    Parameters
    ----------
    file : str
        Path of CSV file
    european : bool
        True if CSV uses ; to separate.
        Default is False
    """
    data = read_csv(file, european)
    values = []
    for i in data:
        try:
            values.append(i[1])
        except IndexError:
            continue
    fig, ax = plt.subplots()
    plt.hist(values, color='red', label=values)
    ax.title.set_text('Histogram')
    ax.set_xlabel('Status')
    ax.set_ylabel('Number of genes')
    ax.legend()
    plt.show()


def read_csv(file_name, european=False):
    """
    Lees een csv file in en zet deze om naar een lijst van lijsten.

    Parameters
    ----------
    file_name : str
        Naam van het csv file
    european : bool
        True als het csv file een ; als scheidingsteken gebruikt
        Default is False
    Returns
    -------
    csv: list
        Lijst van lijsten met de data uit het csv file
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
    """
    Runs the code
    """
    ### OPDRACHT 1 ###
    # Gebruik de lijsten x y en z voor de grafieken van opdracht 1
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 6, 8, 10, 12, 12, 4, 14, 7, 10]
    z = []
    for i in range(0, 10):
        n = random.randint(1, 100)
        z.append(n)

    opdracht_1(x, y, z)

    # OPDRACHT 2 #
    # Bestand voor opdracht 2
    patienten = "patienten.csv"
    opdracht_2(patienten)

    # OPDRACHT 3 #
    # Bestand voor opdracht 3
    gist = "yeast_genes.csv"
    opdracht_3(gist)

    # OPDRACHT 4 #
    # Bestand voor opdracht 4
    test = "test.csv"
    opdracht_3(test, True)


if __name__ == "__main__":
    main()
