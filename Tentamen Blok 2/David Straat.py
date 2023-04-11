import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import os
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Code for displaying the graph in a tkinter screen found at
# https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html


class GUI(tk.Tk):
    """
    This class creates a GUI and allows the user to select a file, it then
    reads the file and puts the contents in an attribute called content.

    Parameters:
    ----------
    file_format: str
    the file_format of the file to be read, can be either 'GFF3' or 'FASTA'

    Attributes:
    ----------
    content: str or list
    the contents of the file, either a list of lists (in the case of a GFF3)
    or a string (in the case of a FASTA)

    filename: str
    the path of the file that was selected

    file_format: str
    the format of the file to be read, can be either 'GFF3' or 'FASTA'
    """

    def __init__(self, file_format):
        super().__init__()
        # Creates the window
        self.content = None
        self.filename = None
        self.file_format = file_format
        self.title('Import a file')
        self.resizable(True, True)
        self.geometry('150x150')
        # Creates the button
        self.open_button = ttk.Button(
            self,
            text=f'Select a {file_format} file',
            command=self.select_file
        )
        self.open_button.pack()
        self.mainloop()

    def select_file(self):
        """
        This function runs a Filedialog that requires you to open a file, and
        depending on the file_format attribute, runs GUI.read_gff3 or
        GUI.read_fasta
        """
        # Opens a file dialog
        filename = fd.askopenfilename(
            title=f'Open a {self.file_format} file',
            initialdir=os.getcwd())
        self.destroy()
        self.filename = filename
        # Directs the file path to the correct function that reads the
        # associated file
        if self.file_format == 'GFF3':
            self.read_gff3()
        elif self.file_format == 'FASTA':
            self.read_fasta()
        else:
            showinfo('Invalid file', 'Invalid file requested in code, please'
                                     'contact the developer')

    def read_gff3(self):
        """
        Reads a GFF3 file specified and saves it in a 2d list as self.content
        """
        # Checks if the file is a GFF3 file
        if self.filename.upper().endswith('.GFF3'):
            # Tries to open the file and put the information in a 2d list
            content = []
            try:
                with open(self.filename) as file:
                    for line in file:
                        if not line.startswith('#'):
                            data = line.split('\t')
                            content.append(data)
                self.content = content
            except FileNotFoundError:
                showinfo('File not found', 'File not found')
        # If the file is not a GFF3 file, create a popup and open the dialog
        # screen again.
        elif self.filename == '':
            showinfo('No file selected', 'No file was selected')
            self.__init__('GFF3')
        else:
            showinfo('Invalid file', 'File is not a .GFF3 file')
            self.__init__('GFF3')

    def read_fasta(self):
        """
        Reads a FASTA file specified and saves it in a string as self.content
        """
        fasta_extensions = ['.FNA', '.FAA', '.FASTA', '.FFN', '.FRN', '.FA']
        # Checks if the file is a FASTA file
        if self.filename.upper().endswith(tuple(fasta_extensions)):
            # Tries to open the file and put the information in a string
            try:
                with open(self.filename) as file:
                    data = file.readlines()[1:]
                    content = ''.join(data).replace('\n', '')
                self.content = content
            except FileNotFoundError:
                showinfo('File not found', 'File not found')
        # If the file is not a FASTA file, create a popup and open the dialog
        # screen again.
        elif self.filename == '':
            showinfo('No file selected', 'No file was selected')
            self.__init__('FASTA')
        else:
            showinfo('Invalid file', 'File is not a .FASTA file')
            self.__init__('FASTA')


def new_fasta(GFF3, FASTA, filename='new_fasta.fasta'):
    """
    Generates a new FASTA file containing the genes listed in the GFF3 file
    from the genetic code described in the FASTA file provided

    Parameters:
    ----------
    GFF3: class
    The class used previously to open and read the GFF3 file

    FASTA: class
    The class used previously to open and read the FASTA file

    filename: str
    The name of the file to be created

    Returns:
    -------
    None
    """
    # Try to open a file to write to.
    try:
        with open(filename, 'w') as file:
            for entry in GFF3.content[1:]:
                # Gets the start and end positions and name of the gene
                # from the GFF3 file, and the genetic code from the FASTA
                # file and puts this into a FASTA format, before putting these
                # into the new FASTA file.
                try:
                    if entry[2] == 'gene':
                        name = entry[8]
                        start = int(entry[3]) - 1
                        end = int(entry[4]) - 1
                        gene_code = '\n'.join(
                            entry.strip() for entry in re.findall(
                                r'.{1,70}(?:\s+|$)', FASTA.content[start:end]))
                        gene_entry = f'>{name}\n{gene_code}\n\n'
                        file.write(gene_entry)
                except IndexError:
                    break
    except FileNotFoundError:
        showinfo('Could not write to file',
                 f'Could not write to file {filename}')


def visualize_features(GFF3, consensus_is_present, consensus_sequence):
    """
    Generates a histogram of the features in the GFF3 file

    Parameters:
    ----------
    GFF3: class
    The class used previously to open and read the GFF3 file

    Returns:
    -------
    None
    """
    # Creates a list of the features in the GFF3 file
    features = []
    for index in range(len(GFF3.content)):
        try:
            features.append(GFF3.content[index][2])
        except IndexError:
            break
    # Checks if the consensus sequence given is present
    if consensus_is_present:
        message = f'The consensus sequence, {consensus_sequence}, was found ' \
                  f'in the FASTA file'
    else:
        message = f'The consensus sequence, {consensus_sequence}, was not ' \
                  f'found in the FASTA file'

    # Creates a new window that displays a histogram with the frequency of the
    # features in the GFF3 file and a message that tells if the consensus
    # sequence was found in the FASTA file.
    display = tk.Tk()
    display.dimensions = '800x600'
    display.resizable(True, True)
    display.title('Feature visualization')
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure.add_subplot(111).hist(features)
    figure.axes[0].set_title('Features in GFF3 file')
    figure.axes[0].set_xlabel(f'Features')
    figure.axes[0].set_ylabel('Frequency')
    canvas = FigureCanvasTkAgg(figure, master=display)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill='both', expand=True)
    label = tk.Label(display, text=message)
    label.pack()
    display.mainloop()


def find_consensus(FASTA, consensus):
    """
    Determines if the consensus sequence provided is present in the FASTA file

    Parameters:
    ----------
    FASTA: class
    The class used previously to open and read the FASTA file

    Returns:
    -------
    bool
    True if the consensus sequence is present in the FASTA, False if the
    consensus sequence is not present in the FASTA
    """
    consensus = consensus.upper()
    # Translates the consensus sequence given into a REGEX pattern
    Abbreviation_codes = {
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'T': 'T',
        'U': 'U',
        'W': '[AT]',
        'S': '[CG]',
        'M': '[AC]',
        'K': '[GT]',
        'R': '[AG]',
        'Y': '[CT]',
        'B': '[CGT]',
        'D': '[AGT]',
        'H': '[ACT]',
        'V': '[ACG]',
        'N': '[ACGTU]'
    }
    for symbol in consensus:
        if symbol in Abbreviation_codes:
            consensus = consensus.replace(symbol, Abbreviation_codes[symbol])
    x = re.search(consensus, FASTA.content)
    if x:
        return True
    else:
        return False


def main():
    consensus_sequence = 'wTTTrAATt'
    FASTA = GUI('FASTA')
    GFF3 = GUI('GFF3')
    try:
        new_fasta(GFF3, FASTA)
        consensus_is_present = find_consensus(FASTA, consensus_sequence)
        visualize_features(GFF3, consensus_is_present, consensus_sequence)
    except TypeError:
        print('No file was selected')


main()
print('Done')