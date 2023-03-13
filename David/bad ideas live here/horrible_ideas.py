from tkinter.messagebox import showwarning
import random
import winsound as ws
import webbrowser
import urllib.request
import pathlib
import ctypes
import threading
import webview


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
        showwarning('PANIC!', 'A' * random.randint(1, 1000))
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


def brrrrrr(num):
    """
    Will run itself 2^num times. Will crash your computer if num is too high.

    Parameters
    ----------
    num : int

    Returns
    -------
    None
    """
    print(num)
    num -= 1
    if num > 0:
        brrrrrr(num)
        brrrrrr(num)


def setBackground(url):
    """
    sets the background of the desktop to the image at the url

    Parameters
    ----------
    url : str
        the url of the image to be set as the background

    Returns
    -------
    None
    """
    urllib.request.urlretrieve(url, "image.png")
    path = f"{pathlib.Path('image.png').parent.resolve()}\image.png"
    print(path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path,
                                               0)

def UhOh(threads):
    Thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=panicPopUp)
        t.daemon = True
        Thread_list.append(t)

    for i in range(threads):
        Thread_list[i].start()

    showwarning('PANIC!', 'A' * random.randint(1, 1000))

def Rickroll():
    webview.create_window('Never gonna give you up', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    webview.start()

def weee(num):
    for _ in range(num):
        Rickroll()

weee(3)