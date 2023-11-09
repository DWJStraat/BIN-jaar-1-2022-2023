"""
A script written by David Straat for generating
a sequence consensus and profile.
"""


def most_frequent(input_list):
    """
    Determines the most frequent item in a list.
    parameters:
    ----------
    input_list: list
        the list to be used.
    Returns:
    -------
    most_frequent: str
        the most frequent item in the list.
    """
    return max(set(input_list), key=input_list.count)


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
    output_list : List
        The contents of the file, in a list of strings, separated at the
        headers.
    """
    with open(file_name) as file:
        content = file.readlines()[1:]
        full_sequence = ""
        for line in content:
            if line[0] != ">":
                full_sequence += line.strip()
            else:
                full_sequence += "\n"
        output_list = full_sequence.split("\n")
    return output_list


def consensus_generator(input_list):
    """
    Determines the consensus sequence of a set of sequences.
    Parameters:
    ----------
    input_list: list, the list of sequences to be used.

    Returns:
    -------
    consensus: str, the consensus sequence.
    """
    for i in range(len(input_list[0])):
        column = []
        for sequence in input_list:
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


if __name__ == "__main__":
    main(True)
