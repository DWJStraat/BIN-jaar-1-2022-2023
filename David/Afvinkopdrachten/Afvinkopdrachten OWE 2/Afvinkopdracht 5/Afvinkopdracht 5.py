import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import Afvinkopdracht5_class as a5


def select_file():
    """
    Select a file from the file dialog

    Parameters:
    ----------
    None

    Returns:
    -------
    filename: str
        The name of the file selected
    """
    filename = fd.askopenfilename(
        title='Open a file'
        # initialdir=r'C:\Users\dstra\OneDrive -
        # HAN\Projectgroep_9\Eno1_FASTAs'
    )
    return filename


def multiple_fna(file_name):
    """
    Opens an FNA file, and returns the contents as a list of strings
    separated at the headers.

    Parameters
    ----------
    file_name : Str
        The path of the file to be opened.

    Returns
    -------
    outlist : List
        The contents of the file, in a list of strings, separated at the
        headers.
    """
    print("Opening file...")
    with open(file_name) as file:
        content = file.readlines()
        full_sequence = ""
        for line in content:
            if line[0] != ">":
                full_sequence += line.strip()
            else:
                full_sequence += f"\n{line.strip()}|"
        outlist = full_sequence.split("\n")
    print('File opened!')
    return outlist[1:]


def backend():
    objectlist = []
    filename = select_file()
    for i in multiple_fna(filename):
        templist = i.split('|')
        tempobject = a5.fasta()
        tempobject.setHeader(templist[0])
        tempobject.setSequence(templist[1])
        objectlist.append(tempobject)
    highestgc = 0
    highestgcobject = None
    for j in objectlist:
        tempDna = a5.DNA(j.getSequence())
        if tempDna.getGcPercent() > highestgc:
            highestgc = tempDna.getGcPercent()
            highestgcobject = j
    showinfo(
        title='Highest GC content',
        message=f'The sequence with the highest GC content is \n'
                f'{highestgcobject.getHeader()}\n with a GC content'
                f' of {highestgc * 100:.2f}%')
    highestgcobjectdna = a5.DNA(highestgcobject.getSequence())
    print(f'Header: {highestgcobject.getHeader()}\nGC percentage: '
          f'{highestgc * 100:.2f}%\nTranscript: '
          f'{highestgcobjectdna.getTranscript()}\nLength: '
          f'{highestgcobjectdna.getLength()}')


def main():
    root = tk.Tk()
    root.title('Object Oriented DNA Sequence Analyzer')
    root.resizable(True, True)
    root.geometry('150x150')
    open_button = ttk.Button(root, text='Open file', command=backend)
    open_button.pack(expand=True)

    # run the application
    root.mainloop()


main()
