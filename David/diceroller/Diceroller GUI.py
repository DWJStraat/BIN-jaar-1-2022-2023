# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:54:17 2021

@author: David
"""

# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Diceroller import roll

# Create an instance of tkinter frame
win= Tk()
textvar = StringVar()
# Set the size of the tkinter window
win.geometry("700x350")

# Define a function to show the popup message
def show_msg(a):
    if(len(a) > 0):
        rollmult = a
    else:
        rollmult = [1]
    results, rolls = roll(6,rollmult[0])
    messagebox.showinfo("Message",results)
    print(rollmult)
   
def mywarWritten(*args):
    print ("mywarWritten",textvar.get())
    stringinput = textvar.get()
    listoutput = [int(s) for s in stringinput.split() if s.isdigit()]
    print(listoutput)
    return listoutput



# Add an optional Label widget
Label(win, text= "Welcome Folks!", font= ('Aerial 17 bold italic')).pack(pady= 30)
Entry(win,textvariable=textvar).pack(pady=15)

textvar.trace("w",mywarWritten)
listoutput = mywarWritten()






# Create a Button to display the message
ttk.Button(win, text= "Click Here", command=show_msg).pack(pady= 20)
win.mainloop()
