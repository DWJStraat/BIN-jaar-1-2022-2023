import re
import time


def read_fna(file_name):
    """
    Opens a FNA file, and returns the contents as a single string.

    Parameters
    ----------
    file_name : Str
        The path of the file to be opened.

    Returns
    -------
    string : Str
        The contents of the file, in a single string.

    """
    # Opens the file
    with open(file_name, 'r') as file:
        # Removes the header
        line = file.readlines()[1:]
        # Removes extra spaces and newlines
        string = ''.join(line).strip()
        string = ''.join(string.splitlines())
    return string


def dna_check_regex(string):
    """
    Checks if a string is a valid DNA sequence.

    Parameters
    ----------
    string : Str
        The string to be checked.

    Returns
    -------
    bool
        True if the string is a valid DNA sequence, False otherwise.

    """
    # Checks if the string is a valid DNA sequence
    x = re.search('^[ATCGN]*$', string)
    return x


def dna_check_iterate(string):
    """
    Checks if a string is a valid DNA sequence.

    Parameters
    ----------
    string : Str
        The string to be checked.

    Returns
    -------
    bool
        True if the string is a valid DNA sequence, False otherwise.

    """
    # Checks if the string is a valid DNA sequence
    for char in string:
        if char not in 'ATCGN':
            return False
    return True


def main():
    start = time.time()
    fna = read_fna("Mus_musculus.GRCm38.dna.chromosome.1.fa")
    endfna = time.time()
    print('Finished loading. Starting regex...')
    startregex = time.time()
    dna_check_regex(fna)
    endregex = time.time()
    print('Finished regex. Starting iterate...')
    startiterate = time.time()
    dna_check_iterate(fna)
    enditerate = time.time()
    print("Regex: ", endregex - startregex)
    print("Iterate: ", enditerate - startiterate)
    print('FNA: ', endfna - start)


main()
