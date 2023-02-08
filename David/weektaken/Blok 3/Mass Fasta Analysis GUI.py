import contextlib
import tkinter
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import json

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from fasta_class import Fasta
import glob
import os


class GUI_entry:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Mass Fasta Analysis")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.virus_code = tkinter.StringVar()
        self.virus_code.set("")
        self.config = self.loadConfig()
        self.path_var = self.config["path"]
        self.file_list = []

        self.path_label = tkinter.Label(self.root,
                                        text=f"Path:\n{self.path_var}",
                                        bg="white")
        self.path_label.pack()

        self.set_path_button = tkinter.Button(self.root,
                                              text="Set path",
                                              command=self.setPath)
        self.set_path_button.pack()

        self.load_button = tkinter.Button(self.root,
                                          text="Load",
                                          command=self.load)
        self.load_button.pack()

        self.description_label = tkinter.Label(self.root,
                                               text="\nThis program will load "
                                                    "all fasta files in the\n"
                                                    "selected folder and "
                                                    "analyse them.",
                                               bg="white")
        self.description_label.pack()

        self.root.mainloop()

    def loadConfig(self):
        with open("config.json", 'r') as file:
            return json.load(file)

    def setPath(self):
        self.path_var = fd.askdirectory()
        self.path_label.config(text=f"Path: {self.path_var}")
        self.config["path"] = self.path_var
        with open("config.json", 'w') as file:
            json.dump(self.config, file)

    def load(self):
        print('Loading...')
        os.chdir(self.path_var)
        for file in glob.iglob("**/*.fna", recursive=True):
            self.file_list.append({file})
        GUI_analyse(self.file_list, self.path_var)

    def quit(self):
        self.root.destroy()


class GUI_analyse:
    def __init__(self, file_list, path):
        self.file_list = file_list
        self.path = path
        self.root = tkinter.Tk()
        self.root.title("Mass Fasta Analysis")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.fasta = None

        self.description_label = tkinter.Label(self.root,
                                               text="Select a file to analyse",
                                               bg="white")
        self.description_label.pack()

        self.buttons()

        self.root.mainloop()

    def buttons(self):
        self.file = tkinter.StringVar(self.root)
        self.file.set(self.file_list[0])

        self.file_selection = tkinter.OptionMenu(self.root, self.file,
                                                 *self.file_list)
        self.file_selection.pack()

        self.analyse_button = tkinter.Button(self.root,
                                             text="Analyse",
                                             command=self.analyse)

        self.analyse_button.pack()

        self.mass_analyse_button = tkinter.Button(self.root,
                                                  text="Mass analyse",
                                                  command=self.mass_analyse)

        self.mass_analyse_button.pack()

    def analyse(self):
        self.fasta_name = self.file.get()[2:-2]
        with contextlib.suppress(AttributeError):
            self.GC_calc_button.destroy()
            self.plot_button.destroy()
        print(self.file.get()[1:-1])
        path = f'{self.path}/{self.fasta_name}'
        self.fasta = Fasta(path)
        self.fasta.loadFile(self.fasta.type)
        if self.fasta.type in ['complete', 'coding']:
            self.GC_calc_button = tkinter.Button(self.root,
                                                 text="GC content",
                                                 command=self.GC_calc)
            self.GC_calc_button.pack()

            self.plot_button = tkinter.Button(self.root,
                                                text="Plot",
                                                command=self.gcplot)
            self.plot_button.pack()

            self.fasta.calcGC()
            self.GC = self.fasta.GC_percent

    def mass_analyse(self):
        for file in self.file_list:
            self.fasta = Fasta(file)
            self.GC = self.fasta.calcGC()
            self.fasta = None

    def GC_calc(self):
        print("Calculating GC content...")

        print(self.GC)
        if self.GC is None:
            showinfo("GC content", "No GC content found")
        elif type(self.GC) is dict:
            total = self.fasta.GC_average
            print(f'Total:{total}')
            showinfo("Total GC content",
                     f"Total GC content:\n{total * 100:.2f}%")
        else:
            showinfo("GC content", f"GC content:\n{self.GC * 100:.2f}%")

    def gcplot(self):
        plot = self.fasta.plotGC()
        if plot is None:
            showinfo("GC content", "No GC content found")
        elif type(plot) is dict:
            print('foobar')
        else:
            plotGUI(self.fasta_name, plot, 'plot')


    def quit(self):
        self.root.destroy()

class plotGUI:
    def __init__(self, name, plot, type):
        self.root = tkinter.Tk()
        self.root.title("Mass Fasta Analysis")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        self.root.configure(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        if type == 'plot':
            self.plot(plot)
        elif type == 'table':
            self.table(plot)
        self.description_label = tkinter.Label(self.root,
                                               text="Select a file to analyse",
                                               bg="white")
        self.description_label.pack()
        self.root.mainloop()


    def plot(self, plot):
        fig = plot.figure(1)
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def table(self, plot):
        pass

    def quit(self):
        self.root.destroy()


if __name__ == "__main__":
    GUI_entry()
