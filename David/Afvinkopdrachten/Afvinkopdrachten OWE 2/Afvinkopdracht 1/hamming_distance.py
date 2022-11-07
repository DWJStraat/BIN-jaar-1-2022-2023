

def main(training = False):
    '''
    Counts the hamming distance between two sequences.
    Variables:
        training: boolean, if True, the training file is used, if False, the test file is used.
    '''
    # Some empty variables to be used later
    list = []
    count = 0
    # Defining the file names
    training_file = "hamming_distance_training.fa"
    test_file = "hamming_distance_test.fa"
    # If training is True, the training file is used, if False, the test file is used.
    if training == True:
        filename = training_file
    else:
        filename = test_file
    # Opening the file
    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            list.append(line.strip())
    # Counting the differences between the two sequences
    for i in range(len(list[0])):
        if list[0][i] != list[1][i]:
            count += 1
    # Printing the result
    print(count)


main()