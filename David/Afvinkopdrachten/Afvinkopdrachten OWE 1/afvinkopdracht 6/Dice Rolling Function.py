# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:38:12 2022

@author: dstra
"""

import random


def roll(number_of_throws, sides=6):
    '''
    This function rolls a number of dice

    Parameters
    ----------
    number_of_throws : Int
        How many dice should be rolled.
    sides : Int, optional
        How many sides the die should have. The default is 6.

    Returns
    -------
    rolls : List of Ints
        The results of the dice rolls.

    '''
    rolls = []
    for i in range(0, number_of_throws):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls


def main(advanced=False):
    '''
    Allows the user to enter an amount of dice to roll, and outputs a list
    of rolls. In advanced mode, allows the user to select the sides of the
    die

    Parameters
    ----------
    advanced : Bool, optional
        Allows you to enable Advanced Mode, which allows you to pick the sides 
        of the die. The default is False.

    Returns
    -------
    None.

    '''
    if advanced == False:
        number_of_throws = int(
            input('How many dice would you like to roll?\n'))
        sides = 6
    else:
        xdy = input(
            'Please enter a diceroll in the formay (X)D(Y)(Example: 1D6)\n')
        xdy = xdy.upper()
        number_of_throws, sides = xdy.split('D')
        number_of_throws = int(number_of_throws)
        sides = int(number_of_throws)
    rolls = roll(number_of_throws, sides)

    print(rolls)


main()
