# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:20:14 2022

@author: dstra
"""

def is_prime(number):
    prime = True
    if number > 1:
        for number2 in range(2, number//2):
            if number % number2:
                prime = False
    return prime

def main():
    number = int(input('Enter any number greater than 0: \n'))
    prime = is_prime(number)
    if prime == True:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')
main()