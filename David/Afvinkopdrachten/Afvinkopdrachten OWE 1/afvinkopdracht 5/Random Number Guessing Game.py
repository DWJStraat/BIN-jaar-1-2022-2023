import random


def rand_number_game(wins):
    """
    Plays a game where the user has to guess a random number between 1 and 100
    Parameters
    ----------
    wins : int the amount of times the user has won

    Returns
    -------

    """
    number = random.randint(1, 100)
    guessed = False
    while not guessed:
        guess = int(input('Guess a number:\n'))
        if guess > number:
            print('\nToo high, try again.')
        elif guess < number:
            print('\nToo low, try again.')
        else:
            wins += 1
            print(
                f'Yes, {number} is correct!\nYour score is {wins}.\n'
                f'Play again?')
            guessed = True
    return wins


def main():
    """
    Plays the game until the user decides to stop
    """
    wins = 0
    play = True
    while play:
        wins = rand_number_game(wins)
        playing = input('Y/N\n').upper()
        if playing == 'N':
            play = False
            print(f'Thank you for playing! Your score was{wins}')


main()
