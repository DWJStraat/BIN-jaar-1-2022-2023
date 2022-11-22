import random
import tabulate
import time

def generateBingoCard(maxno = 100, collumn = 5, row = 5, freeslot = True, freex = 2, freey = 2):
    card = []
    numbers = []
    for i in range(maxno):
        numbers.append(i)
    for i in range(collumn):
        card.append([])
        for j in range(row):
            if freeslot == True and freex == i and freey == j:
                card[i].append("Free")
            else:
                no = random.choice(numbers)
                numbers.remove(no)
                card[i].append(no)
    return card

def main(cards = 1):
    file = open(f'Bingocard {time.strftime("%d-%m-%Y %H-%M-%S")}.txt', 'w')
    for i in range(cards):
        print(tabulate.tabulate(generateBingoCard(), tablefmt="grid"))
        file.write(tabulate.tabulate(generateBingoCard(), tablefmt="grid"))
        print("")
        file.write("~~~")
    file.close

main(3)