# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:49:02 2022

@author: dstra
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

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
    string = HORUS.Read.fna(filename)
    types = HORUS.identify.dna(string)
    if types:
        GC100, length = HORUS.tutor_tasks.weekopdracht_2(filename)
        message=f'GC% = {GC100}% Length = {length}'
        HORUS.QR.generator(message, 'output')
        showinfo(
            title='Weektaak 3 : DNA',
            message=message
            )
        
        
    else:
        length, d, e, r, k, dp, ep, rp, kp, charge = HORUS.tutor_tasks.weekopdracht_3(filename)
        weight = HORUS.tutor_tasks.weektaak_4(filename)
        message=f'D : {d}, E : {e}, R : {r}, K : {k}\nD%: {dp*100:.2f}%, E%: {ep*100:.2f}%, R%: {rp*100:.2f}%, K%: {kp*100:.2f}%\nLength = {length}, Charge = {charge}\nWeight = {weight/1000:.3f} kDa'
        HORUS.QR.generator(message, 'output')
        showinfo(
            title='Weektaak 3 : Protein',
            message=message
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
