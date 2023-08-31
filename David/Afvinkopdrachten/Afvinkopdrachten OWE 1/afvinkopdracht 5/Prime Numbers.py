# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:20:14 2022

@author: dstra
"""


def is_prime(number):
    """
    Checks if a number is prime
    Parameters
    ----------
    number : int

    Returns
    -------
    prime : bool
    """
    prime = True
    if number > 1:
        for number2 in range(2, number // 2):
            if number % number2:
                prime = False
    return prime


def main():
    """
    Asks for a number and checks if it is prime
    Returns
    -------
    None.

    """
    number = int(input('Enter any number greater than 0: \n'))
    if is_prime(number):
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')


main()
