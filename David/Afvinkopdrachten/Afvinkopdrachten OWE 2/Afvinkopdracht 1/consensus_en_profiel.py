def most_frequent(list):
    '''
    Determines the most frequent item in a list.
    Variables:
        list: list, the list to be used.
    '''
    return max(set(list), key = list.count)

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

def consensusGenerator(list):
    for i in range(len(list[0])):
        column = []
        for sequence in list:
            column.append(sequence[i])
        print(most_frequent(column), end = "")


def main(training = False):
    '''
    Determines the consensus sequence of a set of sequences.
    Variables:
        training: boolean, if True, the training file is used, if False, the test file is used.
    '''
    # Defining the file names
    training_file = "consensus_en_profiel_training.fa"
    test_file = "consensus_en_profiel_test.fa"
    # If training is True, the training file is used, if False, the test file is used.
    if training == True:
        filename = training_file
    else:
        filename = test_file
    # Opening the file
    list = multipleFna(filename)
    # Determining the consensus sequence
    consensusGenerator(list)


main(True)