def fna(file_name):
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


def multipleFna(file_name):
    """
    Opens a FNA file, and returns the contents as a list of strings separated
    at the headers.

    Parameters
    ----------
    file_name : Str
        The path of the file to be opened.

    Returns
    -------
    list : List
        The contents of the file, in a list of strings, separated at the
        headers.
    """
    with open(file_name, "r") as file:
        content = file.readlines()[1:]
        full_sequence = ""
        for line in content:
            if line[0] != ">":
                full_sequence += line.strip()
            else:
                full_sequence += "\n"
        list = full_sequence.split("\n")
    return list


def main():
    complete = fna("complete.fasta")
    intronen = multipleFna("intronen.fasta")
    for i in intronen:
        complete = complete.replace(i, "")
    print(complete)


main()
