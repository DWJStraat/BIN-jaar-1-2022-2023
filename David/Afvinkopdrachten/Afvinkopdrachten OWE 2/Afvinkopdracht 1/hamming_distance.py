"""
A script written by David Straat for the purpose of determining the
hamming distance between two sequences.
"""


def main(training=False):
    """
    Counts the hamming distance between two sequences.
    Variables:
        training: boolean, if True, the training file is used, if False,
        the test file is used.
    """
    # Some empty variables to be used later
    output_list = []
    count = 0
    # Defining the file names
    training_file = "hamming_distance_training.fa"
    test_file = "hamming_distance_test.fa"
    # If training is True, the training file is used, if False, the
    # test file is used.
    if training:
        filename = training_file
    else:
        filename = test_file
    # Opening the file
    with open(filename) as file:
        content = file.readlines()
        for line in content:
            output_list.append(line.strip())
    # Counting the differences between the two sequences
    for i in range(len(output_list[0])):
        if output_list[0][i] != output_list[1][i]:
            count += 1
    # Printing the result
    print(count)


if __name__ == "__main__":
    main()
