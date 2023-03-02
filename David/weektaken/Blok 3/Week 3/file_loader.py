from tkinter import filedialog as fd
from bias_counter import *
import re

class file_loader(bias):
    def __init__(self, path = None, name = None):
        self.file = fd.askopenfilename() if path is None else path
        self.contents = self.read_file()
        self.string = "".join(self.contents).replace("\n", "")
        super().__init__(self.string, name)

    def read_file(self):
        content = []
        with open(self.file, 'r') as file:
            content.extend(iter(file))
        return content[1:]

    def setup(self):
        self.set_codon_bias()
        self.set_amino_acid_bias()

class HIV_loader():
    def __init__(self, filename= None, name = None):
        self.externalbias = None
        self.external = []
        self.internal = ''
        self.file = fd.askopenfilename() if filename is None else filename
        self.name = name
        self.contents = self.read_file()

    def read_file(self):
        content = []
        with open(self.file, 'r') as file:
            content.extend(iter(file))
            content = "".join(content)
            content.replace ('\n', '')
            if content.startswith('>'):
                content = content.split('>')
                content.pop(0)
                outlist = []
                for i in content:
                    i = i.split('\n')
                    name = i[0]
                    seq = "".join(i[1:])
                    outlist.append([name, seq])
        return outlist

    def sort(self):
        for i in self.contents:
            external = re.search("protein=Envelope surface glycoprotein", i[0])
            if external is not None:
                self.external += i
            else:
                self.internal += i[1]

    def setup(self):
        self.internalbias = bias(self.internal, self.name+"_internal")
        self.externalbias = bias(self.external[1], self.name+"_external")

