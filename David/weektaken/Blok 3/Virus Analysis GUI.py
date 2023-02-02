import tkinter
from tkinter.messagebox import showinfo
import json
from virus_class import VirusAnalysis

class GUI_entry:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Virus analyzer")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.virus_code = tkinter.StringVar()
        self.virus_code.set("")
        self.config = self.loadConfig()
        self.path_var = self.config["path"]

        self.virus_code_label = tkinter.Label(self.root, text="Virus code", bg="white")
        self.virus_code_label.pack()

        self.virus_code_entry = tkinter.Entry(self.root, textvariable=self.virus_code)
        self.virus_code_entry.pack()

        self.load_button = tkinter.Button(self.root, text="Load", command=self.load)
        self.load_button.pack()

        self.root.mainloop()

    def load(self):
        self.virus = VirusAnalysis(self.virus_code.get())
        self.virus.loadAll("fasta")
        showinfo(title="Virus loaded", message=f"Virus "
                                               f"{self.virus_code.get()} "
                                               f"loaded\nOpening new "
                                               f"window...")
        GUI_analyse(self.virus, self.virus_code)

    def loadConfig(self):
        with open("config.json", 'r') as file:
            return json.load(file)

    def quit(self):
        self.root.destroy()

class GUI_analyse:
    def __init__(self, virus, virus_code):
        self.root = tkinter.Tk()
        self.root.title(f"Virus analyzer - {virus_code.get()}")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.virus = virus

        options = ["Complete", "Coding", "Protein"]
        self.selected = tkinter.StringVar()
        self.dropdown = tkinter.OptionMenu(self.root, self.selected, *options)
        self.dropdown.pack()

        self.gc_button = tkinter.Button(self.root, text="GC content", command=self.gc)
        self.gc_button.pack()

        self.root.mainloop()

    def gc(self):
        print(self.virus.gcContent(self.selected.get()))