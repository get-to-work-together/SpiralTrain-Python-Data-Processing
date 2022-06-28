#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:21:03 2022

@author: peter
"""


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print(f"\nFlight booked from {fromairport} to {toairport}")
    print(f"Number of adults: {numadults}")
    print(f"Number of children: {numchildren}")


#----------------------------------

book_flight(fromairport = "BRS", 
            numadults = 2, 
            numchildren = 2, 
            toairport = "VER")


d = {'fromairport': 'BRS',
     'numadults': 2, 
     'numchildren': 2, 
     'toairport': 'VER'}

book_flight(**d)


#%%

import utils
print( utils.calculate_bmi(90, 1.80) )

from utils import calculate_bmi
print( calculate_bmi(90, 1.80) )

#%%

factor = 3

def maximum(*numbers, factor = 1):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return factor * highest

print( maximum(1,6,2,8,3,9,4, factor = factor) )

#%%

def minmax(*numbers):
    lowest = numbers[0]
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return lowest, highest


print( minmax(1,6,2,8,3,9,4) )

#%%

import pandas as pd

print( pd.read_csv('data.csv', sep = ';') )


















