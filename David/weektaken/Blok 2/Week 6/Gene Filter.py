import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
import sys
from Gene_Filter_Class import File




def notGUI():
    data = File('21213_exome_hcdiffs.txt')
    print('Total entries')
    print('-------------')
    print(data.countEntries())

    data.omimFilter('Retinitis')
    print('Retinitis entries')
    print('-------------')
    print(data.countEntries())

    data.filter('Retinitis')
    print('Candidate Genes')
    print('---------------')
    print(data.countEntries())
    name = data.names()
    aminoacid = data.aminoacids()
    return name, aminoacid

def guiBackend(filename, omim = 'Retinitis', dic = False):
    data = File(filename)
    data.filter(omim)
    names = data.names()
    aminoacids = data.aminoacids()
    if dic:
        output = {'Names': names, 'AminoAcid changes': aminoacids}
    else:
        output = [names, aminoacids]
    return output




def selectFile():
    path = fd.askopenfilename()
    if path != '':
        output = guiBackend(path)
        print(output)
        df = pd.DataFrame({'names' : output[0], 'aminoacids' : output[1]})
        print(df)
        show = tk.Tk()
        show.title('Output')
        show.geometry('500x500')
        txt = tk.Text(show)
        txt.pack()
        class PrintToTXT(object):
            def write(self, s):
                txt.insert(tk.END, s)
        sys.stdout = PrintToTXT()
        print(df)
        show.mainloop()

        print(output)
    else:
        showinfo('Error', 'No file selected')


def main(gui = False):
    if gui:
        root = tk.Tk()
        root.title('Gene Filter')
        root.geometry('500x500')
        root.resizable(False, False)
        open_button = ttk.Button(root, text='Open file', command=selectFile)
        open_button.pack()
        root.mainloop()

    else:
        name, aminoacid = notGUI()
        output = {'Names': name, 'AminoAcid changes': aminoacid}
        print(output)
        return output


a = main()