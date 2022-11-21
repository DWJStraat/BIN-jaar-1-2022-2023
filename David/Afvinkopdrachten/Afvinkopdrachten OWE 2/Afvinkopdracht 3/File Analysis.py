def main():
    wordcount = {}
    file_name = input('Please enter a file name')
    with open(file_name) as file:
        data = file.read()
    print(data)
    data = data.replace('\n', ' ')
    data = data.replace('\t', ' ')
    data = data.split(' ')
    print(data)
    for i in data:
        if i in wordcount:
            wordcount[i] += 1
        else:
            wordcount[i] = 1
    print(wordcount)


main()
