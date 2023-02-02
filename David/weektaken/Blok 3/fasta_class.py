class VirusAnalysis:
    def __init__(self, file_type, file):
        self.file_type = file_type
        self.file = file
        self.type = self.identify(file)
        self.content = None

    def loadFile(self, content):
        if self.file_type == "fasta":
            self.loadFasta(content)
        else:
            print("Invalid filetype")

    def loadFasta(self, content):
        file_contents = self.read()
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


    def read(self):
        contents = []
        with open(self.file, "r") as f:
            contents.extend(line.strip() for line in f)
        return contents

    def calcGC(self):
        sequence = self.content
        if self.type == "complete":
            GC_percent = self.calcGCsingle(sequence)
        elif self.type == "coding":
            GC_percent = {}
            for i in sequence:
                percent = self.calcGCsingle(i[1])
                GC_percent[i[0]] = percent
        elif self.type == "prot":
            print("Does no have a GC%")
            return
        else:
            print("Invalid content")
            return

    def calcGCsingle(self, sequence):
        total = sequence.length
        GC = sequence.count("G") + sequence.count("C")
        return GC/total