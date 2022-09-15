# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:49:02 2022

@author: dstra
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import HORUS

# create the root window
root = tk.Tk()
root.title('Weektaak 3')
root.resizable(True, True)
root.geometry('150x150')


def select_file():
    '''
    This function runs a Filedialog that requires you to open a FASTA, after 
    which it displays the GC% and length of the gene
    '''
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=r'C:\Users\dstra\OneDrive - HAN\Projectgroep_9\Eno1_FASTAs')
    string = HORUS.readfna(filename)
    type = HORUS.typeidentify(string)
    if type == "DNA" :
        GC100, length = HORUS.weekopdracht2(filename)
        showinfo(
            title='Weektaak 3 : DNA',
            message=f'GC% = {GC100}%\nLength = {length}'
            )
    elif type == "Protein":
        length, d, e, r, k, dp, ep, rp, kp, charge = HORUS.weekopdracht3(filename)
        showinfo(
            title='Weektaak 3 : Protein',
            message=f'D : {d}, E : {e}, R : {r}, K : {k}\nD%: {dp:.2f}%, E%: {ep:.2f}%, R%: {rp:.2f}%, K%: {kp:.2f}%\nLength = {length}, Charge = {charge}'
            )
    



# open button
open_button = ttk.Button(
    root,
    text='Select a FASTA',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()
