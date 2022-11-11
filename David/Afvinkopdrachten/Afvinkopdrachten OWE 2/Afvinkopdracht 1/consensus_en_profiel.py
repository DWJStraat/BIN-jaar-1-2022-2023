def most_frequent(inputlist):
    """
    Determines the most frequent item in a list.
    parameters:
    ----------
    inputlist: list
        the list to be used.
    Returns:
    -------
    most_frequent: str
        the most frequent item in the list.
    """
    return max(set(inputlist), key=inputlist.count)


def multiple_fna(file_name):
    """
    Opens an FNA file, and returns the contents as a list of strings separated
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
        outputlist = full_sequence.split("\n")
    return outputlist


def consensus_generator(inputlist):
    """
    Determines the consensus sequence of a set of sequences.
    Parameters:
    ----------
    inputlist: list, the list of sequences to be used.

    Returns:
    -------
    consensus: str, the consensus sequence.
    """
    for i in range(len(inputlist[0])):
        column = []
        for sequence in inputlist:
            column.append(sequence[i])
        print(most_frequent(column), end="")


def main(training=False):
    """
    Determines the consensus sequence of a set of sequences.
    Variables:
        training: boolean, if True, the training file is used, if False, the
        test file is used.
    """
    # Defining the file names
    training_file = "consensus_en_profiel_training.fa"
    test_file = "consensus_en_profiel_test.fa"
    # If training is True, the training file is used, if False, the test file
    # is used.
    if training is True:
        filename = training_file
    else:
        filename = test_file
    # Opening the file
    output = multiple_fna(filename)
    # Determining the consensus sequence
    consensus_generator(output)


main(True)
