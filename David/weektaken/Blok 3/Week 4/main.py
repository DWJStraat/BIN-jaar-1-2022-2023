from tkinter import filedialog as fd

def openFile():
    """
    Opens a file dialog and returns the path of the selected file.
    """
    return fd.askopenfilenames()

def readfile(path):
    """
    Reads a file and returns the content.
    """
    with open(path, 'r') as f:
        return f.read()

def main():
    file_list = openFile()
    groupI = []
    groupII = []
    for i in file_list:
        name = i.split('/')[-1]
        content = readfile(i)
        content = content.replace('>', '/t>').split('/t')
        return content

a = main()