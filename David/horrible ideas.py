from tkinter.messagebox import showwarning
import random
import winsound as ws
import webbrowser


def panicPopUp():
    """
    Opens pop-ups and plays beeps. Instant panic.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    i = random.randint(1, 100)
    while i > 0:
        frequency = random.randint(1500, 4000)
        duration = random.randint(100, 1000)
        ws.Beep(frequency, duration)
        showwarning('PANIC!', 'A' * random.randint(1, 100000))
        i += random.randint(-5, 5)


def neverGonnaGiveYouUp(integer):
    """
    Opens an amount of tabs with the Rick Astley video "Never Gonna Give You Up".

    Parameters
    ----------
    integer : Int
        The amount of tabs to open.

    Returns
    -------
    None
    """
    while integer > 0:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        integer -= 1
