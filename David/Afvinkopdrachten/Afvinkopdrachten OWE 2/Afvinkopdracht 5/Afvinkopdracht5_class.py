import re


class sequence:
    def __init__(self, dnacode):
        self.sequence = None
        self.setDNA(dnacode)
        __lt__ = self.getLength

    def setDNA(self, dnacode):
        x = re.search('^[AGCTN]*$', dnacode)
        if x:
            self.sequence = dnacode

    def getDNA(self):
        return self.sequence

    def getTranscript(self):
        transcript = ''
        for i in self.sequence:
            if i == 'T':
                transcript += 'U'
            else:
                transcript += i
        return transcript

    def getLength(self):
        return len(self.sequence)

    def getGcPercent(self):
        length = len(self.sequence)
        GC = self.sequence.count('G') + self.sequence.count('C')
        GCpercent = GC / length
        return GCpercent


class fasta:

    def __init__(self):
        self.header = None
        self.sequence = None
        self.type = None

    def setHeader(self, header):
        if header.startswith('>') and not header.isdigit():
            self.header = header
        else:
            print('Invalid header')

    def getHeader(self):
        return self.header

    def setSequence(self, dnacode):
        if re.search('^[AGCTN]*$', dnacode):
            self.sequence = dnacode
        else:
            print('Invalid DNA sequence')

    def getSequence(self):
        return self.sequence


class DNA(sequence):
    def __init__(self, dnaCode):
        super().__init__(dnaCode)


class RNA(sequence):
    def __init__(self, dnaCode):
        super().__init__(dnaCode)

    def getTranslation(self):
        protein = ''
        for i in range(0, len(self.sequence), 3):
            protein += code[self.sequence[i:i + 3]]
        return protein

def multiple_fna(file_name, mbuse = False):
    """
    Opens an FNA file, and returns the contents as a list of strings
    separated at the headers.

    Parameters
    ----------
    file_name : Str
        The path of the file to be opened.

    Returns
    -------
    outlist : List
        The contents of the file, in a list of strings, separated at the
        headers.
    """
    outlist = []
    print("Opening file...")
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            full_sequence = ""
            for line in content:
                if line[0] != ">":
                    full_sequence += line.strip()
                else:
                    full_sequence += f"\n{line.strip()}|"
            outlist = full_sequence.split("\n")
    except FileNotFoundError:
        print("Something went wrong while opening the file.")
        if mbuse:
            mb.showerror("Error", "Something went wrong while opening the file.")
    print('File opened!')
    return outlist[1:]