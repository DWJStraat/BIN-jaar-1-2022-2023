import random
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from PIL import Image


class Bingo:

    def __init__(self, name):
        self.row = None
        self.column = None
        self.numbers = None
        self.seed = 1
        self.name = name

    def generateList(self, amount):
        """
        Generates a list of numbers from 1 to amount
        """
        numbers = []
        for i in range(1, amount + 1):
            numbers.append(i)
        self.numbers = numbers

    def addNumbers(self, numbers):
        """
        Adds a list of new numbers to the list of numbers
        """
        for i in numbers:
            if i not in self.numbers:
                self.numbers.append(i)

    def removeNumbers(self, numbers):
        """
        Removes a list of numbers from the list of numbers
        """
        for i in numbers:
            if i in self.numbers:
                self.numbers.remove(i)

    def printNumbers(self):
        """
        Prints the list of numbers
        """
        print(self.numbers)

    def drawNumbers(self, amount):
        """
        Draws a number from the list of numbers
        """
        draws = []
        for i in range(amount):
            number = random.choice(self.numbers)
            self.numbers.remove(number)
            draws.append(number)
        return draws

    def generateCard(self):
        """
        Generates a bingo card
        """
        card = []
        numbers = self.numbers
        random.seed = self.seed
        for i in range(self.column):
            card.append([])
            for j in range(self.row):
                number = random.choice(numbers)
                card[i].append(number)
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        fig.suptitle(f'Card #{str(self.seed)}', fontsize=40)
        df = pd.DataFrame(
            card)

        table = ax.table(cellText=df.values, loc='center',
                         colWidths=[0.05] * self.column, cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(40)
        table.scale(4, 4)
        fig.tight_layout()
        plt.savefig(f'card_{self.name}_{self.seed}.jpg')
        seed = self.seed
        self.seed += 1
        return card, seed

    def settings(self, column, row):
        try:
            self.column = int(column)
            self.row = int(row)
        except ValueError:
            print("Please enter a number")

    def createGame(self):
        self.settings(5, 5)
        self.generateList(100)

    def save(self):
        """
        Saves the game to a pickle file
        """
        dict =  self.__dict__
        with open(f'{self.name}.bingo', 'wb') as f:
            pkl.dump(dict, f)

    def load(self):
        """
        Loads the game from a pickle file
        """
        with open(f'{self.name}.bingo', 'rb') as f:
            dict = pkl.load(f)
        self.__dict__ = dict

    def printNumbers(self):
        return self.numbers

def main():
    game = Bingo('test')
    print('Creating game')
    game.createGame()
    print('Saving game')
    game.save()
    print('Loading game')
    game.load()
    game.generateCard()
    im = Image.open('card1.jpg')
    im.show()
    return game


