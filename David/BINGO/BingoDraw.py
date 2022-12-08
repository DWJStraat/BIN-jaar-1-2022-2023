import random
import pickle


def bingoBuild(max_numbers=100, filename='bingo.dat'):
    """
    Build a list of numbers for bingo

    Parameters
    ----------
    max_numbers : int
        The maximum number to be used in the bingo game

    filename : str
        The name of the file to save the list of numbers to
        Default: 'bingo.dat'

    Returns
    -------
    None
    """
    numbers = []
    for i in range(1, max_numbers + 1):
        numbers.append(i)
    pickle.dump(numbers, open(filename, 'wb'))


def bingoDraw(filename='bingo.dat', runs=1):
    """
    Draw a number from the list of numbers

    Parameters
    ----------
    filename : str
        The name of the file to save the list of numbers to
        Default: 'bingo.dat'

    runs : int
        The number of times to draw a number

    Returns
    -------
    None
    """
    i = 0
    draws = []
    numbers = pickle.load(open(filename, 'rb'))
    print(len(numbers))
    while i < runs:
        number = random.choice(numbers)
        numbers.remove(number)
        draws.append(number)
        i += 1
    print(len(numbers))
    pickle.dump(numbers, open(filename, 'wb'))
    return draws


def bingoRemove(filename='bingo.dat', numbers=None):
    """
    Remove a number from the list of numbers

    Parameters
    ----------
    filename : str
        The name of the file to save the list of numbers to
        Default: 'bingo.dat'

    numbers : list
        The list of numbers to remove from the list of numbers

    Returns
    -------
    None
    """
    if numbers is None:
        numbers = []
    bingo = pickle.load(open(filename, 'rb'))
    for number in numbers:
        try:
            bingo.remove(number)
        except:
            pass
    pickle.dump(bingo, open(filename, 'wb'))


def bingoLoad(filename='bingo.dat'):
    """
    Load the list of numbers

    Parameters
    ----------
    filename : str
        The name of the file to save the list of numbers to
        Default: 'bingo.dat'

    Returns
    -------
    list
        The list of numbers
    """
    return pickle.load(open(filename, 'rb'))


def bingoSave(filename='bingo.dat', numbers=None):
    """
    Save the list of numbers

    Parameters
    ----------
    filename : str
        The name of the file to save the list of numbers to
        Default: 'bingo.dat'

    numbers : list
        The list of numbers to save
        Default: None

    """
    if numbers is None:
        numbers = []
    pickle.dump(numbers, open(filename, 'wb'))

