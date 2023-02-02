import pathlib


class VirusAnalysis:
    def __init__(self, code):
        self.complete = None
        self.coding = None
        self.prot = None
        self.code = code

    def loadFile(self, file, filetype, content):
        if filetype == "fasta":
            self.loadFasta(file, content)
        else:
            print("Invalid filetype")

    def loadFasta(self, file, content):
        file_contents = self.read(file)
        if content in ["complete", "prot"]:
            contents = "".join(file_contents[1:])
        elif content == "coding":
            first_line = True
            entry = ['', '']
            contents = []
            for line in file_contents:
                if line.startswith(">"):
                    entry = ['', '']
                    if first_line:
                        first_line = False
                    else:
                        contents.append(entry)
                    entry[0] = line
                else:
                    entry[1] += line
        exec(f"self.{content} = contents")

    def identify(self, file_content_list):
        if sum(True for i in file_content_list if i[0].startswith('>')) > 1:
            return "coding"
        elif sum(True for i in file_content_list if i[0].startswith('>')) == 1:
            contents = "".join(file_content_list[1:])
            return "complete" if set(contents) <= set("ATGC") else "prot"


    def read(self, file):
        contents = []
        with open(file, "r") as f:
            contents.extend(line.strip() for line in f)
        return contents

    def loadAll(self, type, path = None):
        home = pathlib.Path.home()
        if type == "fasta":
            if path is not None:
                try:
                    self.loadFasta('{path}\{self.code}_complete.fna', "complete")
                    self.loadFasta('{path}\{self.code}_prot.fna', "prot")
                    self.loadFasta('{path}\{self.code}_coding.fna', "coding")
                except:
                    print("Invalid path")
            else:
                self.loadFasta(
                    rf"{home}\OneDrive - HAN\OWE 3\FASTAs\{self.code}\{self.code}_complete.fna",
                    "complete")
                self.loadFasta(
                    rf"{home}\OneDrive - HAN\OWE 3\FASTAs\{self.code}\{self.code}_prot.fna",
                    "prot")
                self.loadFasta(
                    rf"{home}\OneDrive - HAN\OWE 3\FASTAs\{self.code}\{self.code}_coding.fna",
                    "coding")
        else:
            print("Invalid filetype")

    def calcGC(self, content):
        if content == "complete":
            sequence = self.complete
            GC_percent = self.calcGCsingle(sequence)
        elif content == "coding":
            sequence = self.coding
        elif content == "prot":
            print("Does no have a GC%")
            return
        else:
            print("Invalid content")
            return

    def calcGCsingle(self, sequence):
        total = sequence.length
        GC = sequence.count("G") + sequence.count("C")
        return GC/total