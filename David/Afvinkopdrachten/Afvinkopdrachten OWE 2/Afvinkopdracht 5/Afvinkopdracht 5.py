import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import sys


class fasta:

    def __init__(self):
        self.header = None
        self.sequence = None
        self.type = None

    def setHeader(self, header):
        if header.startswith('>') and not header.isdigit():
            self.header = header
        else:
            print('Invalid header')

    def getHeader(self):
        return self.header

    def setSequence(self, sequence):
        if re.search('^[AGCTN]*$', sequence):
            self.sequence = sequence
        else:
            print('Invalid DNA sequence')

    def getSequence(self):
        return self.sequence


class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def setDNA(self, sequence):
        x = re.search('^[AGCTN]*$', sequence)
        if x:
            self.sequence = sequence

    def getDNA(self):
        return self.sequence

    def getTranscript(self):
        transcript = ''
        for i in self.sequence:
            if i == 'T':
                transcript += 'U'
            else:
                transcript += i
        return transcript

    def getLength(self):
        return len(self.sequence)

    def getGcPercent(self):
        length = len(self.sequence)
        GC = self.sequence.count('G') + self.sequence.count('C')
        GCpercent = GC / length
        return GCpercent


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
        # initialdir=r'C:\Users\dstra\OneDrive - HAN\Projectgroep_9\Eno1_FASTAs'
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
    with open(file_name, "r") as file:
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
        tempobject = fasta()
        tempobject.setHeader(templist[0])
        tempobject.setSequence(templist[1])
        objectlist.append(tempobject)
    highestgc = 0
    highestgcobject = None
    for j in objectlist:
        tempDna = DNA(j.getSequence())
        if tempDna.getGcPercent() > highestgc:
            highestgc = tempDna.getGcPercent()
            highestgcobject = j
    showinfo(
        title='Highest GC content',
        message=f'The sequence with the highest GC content is \n{highestgcobject.getHeader()}\n with a GC content of {highestgc*100:.2f}%')



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
