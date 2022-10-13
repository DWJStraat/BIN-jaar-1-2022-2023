import random

def sentinel():
    run = True
    running = input('Would you like to continue? Y/N:').upper()
    if running == 'N':
        run = False

    return run

def CPUchoice():
    choice = random.randint(0,2)
    choicelist = ['PAPER','SCISSORS','ROCK']
    choicenr = int(choice+1)
    choiceword = choicelist[choice]
    return choicenr, choiceword

def playerchoice(word):
    word = word.upper()
    if word == "ROCK":
        choice = 3
    elif word == "PAPER":
        choice = 1
    elif word == "SCISSORS":
        choice = 2
    return choice

def main():
    playing = True
    wins = 0
    while playing == True:
        CPUpick, CPUword = CPUchoice()
        RPS = input('Rock, paper, scissors?\n')
        playerpick = playerchoice(RPS)
        if playerpick == CPUpick:
            print(f'CPU wins. Current wins: {wins}\n')
        if playerpick > CPUpick:
            wins += 1
            print(f'You win! Current wins: {wins}\n')
        else:
            print ('Draw.\n')
        
        playing = sentinel()

main()