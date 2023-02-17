import contextlib
from tkinter import filedialog as fd

class bias:
    def __init__(self, file = None):
        self.file = self.file_open() if file is None else file
        self.contents = self.read_file()
        self.genes = self.contents_split()


    def read_file(self):
        with open(self.file, 'r') as file:
            return file.read()

    def file_open(self):
        return fd.askopenfilename()

    def contents_split(self):
        split_contents = self.contents.split(">")
        output = []
        with contextlib.suppress(IndexError):
            for i in range(len(split_contents)):
                if split_contents[i] != "":
                    contents =  f'>{split_contents[i]}'.splitlines()
                    output.append([contents[0], "".join(contents[1:]).replace("\n", "")])
        return output


a=bias(r"C:\Users\dstra\OneDrive - HAN\OWE 3\FASTAs\HIV2\HIV2_coding.fna")
