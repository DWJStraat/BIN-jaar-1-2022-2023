import re
import gzip
import datetime


def read_gzip_multiple_fna(path):
    full_code = ''
    with gzip.open(path) as f:
        for line in f:
            line = line.decode('utf-8')
            if line[0] != '>':
                full_code += line.strip()
            else:
                full_code += f'\n{line}|'
    output = full_code.split('\n')
    return output


def multiple_fna(file_name):
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
    print("Opening file...")
    with open(file_name, "r") as file:
        content = file.readlines()
        full_sequence = ""
        for line in content:
            if line[0] != ">":
                full_sequence += line.strip()
            else:
                full_sequence += f"\n{line.strip()}|"
        outlist = full_sequence.split("\n")
    return outlist[1:]


def protCheck(string):
    """
    Checks if a string is a valid protein sequence.

    Parameters
    ----------
    string : Str
        The string to be checked.

    Returns
    -------
    bool
        True if the string is a valid protein sequence, False otherwise.

    """
    # Checks if the string is a valid protein sequence
    x = re.search('^[ARNDCQEGHILKMFPSTWYV]*$', string)
    if x:
        return True
    else:
        return False


def consensus(string):
    """
    Finds the consensus sequence of a protein sequence.

    Parameters
    ----------
    string : Str
        The protein sequence to be checked.

    Returns
    -------
    bool
        True if the string contains the consensus sequence, False otherwise.

    integer The start position of the consensus sequence. If there is no
    start position, returns -1.
    """
    x = re.search('MCNSSC[MV]GGMNRR', string)
    if x:
        return True, x.start()
    else:
        return False, -1


def iterate_and_consensus(gene_list):
    for i in gene_list:
        temp = i.split('|')
        try:
            if protCheck(temp[1]):
                con, consensuspos = consensus(temp[1])
                if con:
                    print(
                        f'Consensus sequence found in gene {temp[0].split(" ")[0]} at position {consensuspos}')
        except IndexError:
            continue


def main():
    start_time = datetime.datetime.now()
    print('Start time:', start_time)
    gene_list = multiple_fna("Mus_musculus.GRCm38.pep.all.fa")
    print('Gene list created after:', datetime.datetime.now() - start_time)
    iterate_and_consensus(gene_list)
    print('Done!')
    print(f'Time taken: {datetime.datetime.now() - start_time}')

main()