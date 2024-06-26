import random
import tabulate

def generateBingoCard(maxno = 100, collumn = 5, row = 5, freeslot = True, freex = 2, freey = 2):
    card = []
    numbers = []
    for i in range(1, maxno):
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
    file = open(f'../Bingocard.txt', 'w')
    for i in range(cards):
        card = generateBingoCard()
        print(tabulate.tabulate(card, tablefmt="grid"))
        file.write(tabulate.tabulate(card, tablefmt="grid"))
        print("")
        if i != cards:
            file.write("\n\n\n")
    file.close()

main(1)