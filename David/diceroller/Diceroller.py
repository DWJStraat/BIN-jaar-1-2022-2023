# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:04:09 2021

@author: David
"""

# import modules
import random
from datetime import datetime
import sys

# variable bin
now = datetime.now()
current_time = now.strftime("%D %H:%M:%S")

# function bin
def roll(x,y):
    # setting/resetting variables
    rolls = []
    result = 0
    while y > 0 :

        roll =  (random.randint(1, x))
        print (roll)
        y = y - 1
        
        # add roll to the total result
        result = result + roll
        
        # add roll to list of component rolls
        rolls.append(roll)
    else :
        print ("total:",result)
    return result, rolls

def logdice(w,x,y,z) :
    # timestamping
    now = datetime.now()
    # print to log (Don't ask me what everything does)
    original_stdout = sys.stdout 
    with open('dicelog.txt', 'a') as f:
        sys.stdout = f 
        print("On", now.strftime("%D %H:%M:%S"), "User rolled a", w, "on", x,"d",y, ". Component rolls:", z)
        sys.stdout = original_stdout
        
def rollmaster(a,b) :
    print ("Rolling the dices...")
    print (f"On a {b}d{a}, you rolled:")
    # rolling dice
    result, rolls = roll(a,b)
    print(result)
    logdice(result, b, a, rolls)
    return result, rolls


if __name__ == "__main__":
    max = int(input("d"))
    multi = int(input("How many times?")) 
    rollmaster(max,multi)
