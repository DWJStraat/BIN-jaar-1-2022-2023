import random


def sentinel():
    """
    Asks the user if they want to continue playing
    Returns
    -------

    """
    running = input('Would you like to continue? Y/N:').upper()
    return running != 'N'


def CPUchoice():
    """
    Chooses a random number between 1 and 3 and returns the number and the word
    Returns
    -------

    """
    choice = random.randint(0, 2)
    choicelist = ['PAPER', 'SCISSORS', 'ROCK']
    choicenr = int(choice + 1)
    choiceword = choicelist[choice]
    return choicenr, choiceword


def playerchoice(word):
    """
    Converts the word to a number
    Parameters
    ----------
    word : str

    Returns
    -------

    """
    word = word.upper()
    if word == "ROCK":
        choice = 3
    elif word == "PAPER":
        choice = 1
    elif word == "SCISSORS":
        choice = 2
    return choice


def main():
    """
    Plays the game until the user decides to stop
    """
    playing = True
    wins = 0
    while playing:
        CPUpick, CPUword = CPUchoice()
        RPS = input('Rock, paper, scissors?\n')
        playerpick = playerchoice(RPS)
        if playerpick == CPUpick:
            print(f'CPU wins. Current wins: {wins}\n')
        if playerpick > CPUpick:
            wins += 1
            print(f'You win! Current wins: {wins}\n')
        else:
            print('Draw.\n')

        playing = sentinel()


main()
