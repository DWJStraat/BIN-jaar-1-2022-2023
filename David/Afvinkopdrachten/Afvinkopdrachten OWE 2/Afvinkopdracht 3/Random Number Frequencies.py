import random
import matplotlib.pyplot as plt


def main():
    counter = 0
    freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0}
    while counter < 100:
        counter += 1
        no = (random.randint(1, 10))
        freq[no] += 1
    print(freq)
    plt.bar(freq.keys(), freq.values())
    plt.show()


main()
