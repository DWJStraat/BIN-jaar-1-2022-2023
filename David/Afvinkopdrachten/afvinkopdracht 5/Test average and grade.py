# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:34:57 2022

@author: dstra
"""

def calc_average(inputlist):
    total = 0 
    length = 0
    # Adds each score in the list to the total and calculates the length
    for score in inputlist:
        total += score
        length += 1
    # Calculates average
    average = total/length
    return average

def determine_grade(score):
    letter = ""
    # Determines letter grade
    if 0 <= float(score) <= 100:     
        if score >= 90:
            letter = 'A'
        elif score >= 80:
            letter = 'B'
        elif score >= 70:
            letter = 'C'
        elif score >= 60:
            letter = 'D'
        else:
            letter = 'F'
    # Prints an error if the number is not in the 0 - 100 range
    else:
         print('ERROR: not a valid grade')
         
    return letter

def main():
    i = 0
    scorelist = []
    letterlist=[]
    run = True
    # Asks up to 5 times for a different grade, and adds this to a list to be put in calc_average later
    while run == True:
        if i < 5:
            i+= 1
            score = int(input(f'Enter your grade for test {i}:\n'))
            scorelist.append(score)
            running = input('Would you like to continue? Y/N:').upper()
            if running == 'N':
                run = False
    for score in scorelist:
        letter = determine_grade(score)
        letterlist.append(letter)
    averagescore = calc_average(scorelist)
    print(f'Your grades are {letterlist}')
    print(f'Your average grade is {averagescore:.2f}, a {determine_grade(averagescore)}.')

main()