import random

def rand_number_game(wins):
    number = random.randint(1, 100)
    guessed = False
    while guessed == False:
        guess = int(input('Guess a number:\n'))
        if guess > number:
            print('\nToo high, try again.')
        elif guess < number:
            print('\nToo low, try again.')
        else:
            wins += 1
            print(f'Yes, {number} is correct!\nYour score is {wins}.\nPlay again?')
            guessed = True
    return wins
        
def main():
    wins = 0
    play = True
    while play == True:
        wins = rand_number_game(wins)
        playing = input('Y/N\n').upper()
        if playing == 'N':
            play = False
            print(f'Thank you for playing! Your score was{wins}')

main()