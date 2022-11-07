# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:50:30 2022

@author: dstra

Function: Generate a random 7 digit lottery number, and outputs this into the
          console.
"""
import random


def lottery_number_generator():
    '''
    Generates a random 7 digit lottery number

    Returns
    -------
    ticket : a 7 digit lottery number, output as a list containing integers

    '''
    counter = 0
    ticket = []
    while counter < 7:
        ticketnumber = random.randint(0, 9)
        ticket.append(ticketnumber)
        counter += 1
    return ticket


def main():
    '''
    Generates a random 7 digit lottery number, and prints the output

    Returns
    -------
    None.

    '''
    ticket = lottery_number_generator()
    ticketlist = [str(int) for int in ticket]
    ticketstring = ''.join(ticketlist)
    print(f'The winning ticket is {ticketstring}')


main()
