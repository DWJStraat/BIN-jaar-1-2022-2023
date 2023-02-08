# Author: David Straat
# Date: 2022-feb-8
# Description : De class voor week 2

import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Week2_class import *
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class GUI:
    def __init__(self):
        self.file_path = None
        self.master = Tk()
        file_path_button = Button(self.master, text="Select file",
                                  command=self.select_file)
        file_path_button.pack()

        self.step = Text(self.master, height=1, width=20)
        self.step.pack()

        ok = Button(self.master, text="OK", command=self.ok)
        ok.pack()

        mainloop()

    def select_file(self):
        self.file_path = fd.askopenfilename()
        print(self.file_path)

    def ok(self):
        if self.file_path in [None, ""]:
            mb.showerror("No file selected", "Please select a file")
            return
        if not self.file_path.endswith(
                ".fasta") and not self.file_path.endswith(".fna"):
            mb.showerror("Wrong file type",
                         "Please select a .fasta or .fna file")
            return
        if self.step != int:
            self.quit()
            display(self.file_path, self.step)

        else:
            mb.showerror("Wrong step type", "Please enter an integer")
            return

    def quit(self):
        self.master.destroy()


class display:
    def __init__(self, file_path, step):
        self.file_path = file_path
        self.step = step

        self.master = Tk()
        self.main = main(self.file_path)
        try:
            self.plot = self.main.plotGC()
        except AttributeError:
            mb.showerror("No GC content found",
                         "No GC content found. Is this a Complete file?")
            self.master.destroy()
            GUI()

        fig = self.plot.figure(1)
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        mean = tkinter.Label(self.master,
                             text="Mean GC content: "
                             f"{self.main.gc_mean * 100:.2f}%", bg="white")
        mean.pack()

        median = tkinter.Label(self.master,
                               text=f"Median GC content: "
                               f"{self.main.gc_median * 100:.2f}%",
                               bg="white")
        median.pack()

        variation = tkinter.Label(self.master,
                                  text=f"Variation:"
                                       f"{self.main.gc_var * 100:.2f}%",
                                  bg="white")
        variation.pack()

        self.master.mainloop()


GUI()
