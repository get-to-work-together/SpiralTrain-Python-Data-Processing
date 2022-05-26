# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:02:18 2022

@author: peter
"""

from random import randint, seed


#%%
seed(1234)

dice1 = randint(1, 6)
dice2 = randint(1, 6)
dice3 = randint(1, 6)
dice4 = randint(1, 6)
dice5 = randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

print(f'The total of 5 throws is {total}')


#%%
seed(1234)

die = []
total = 0
for i in range(5):
    dice = randint(1, 6)
    die.append(dice)
    total += dice

print(f'The total of 5 throws is {total}')


#%%
seed(1234)

die = {}
total = 0
for i in range(5):
    dice = randint(1, 6)
    die[f'throw{i}'] = dice
    total += dice

print(f'The total of 5 throws is {total}')


#%%

seed(1234)

die = []
for _ in range(5):
    die.append(randint(1, 6))

total = sum(die)

print(f'The total of 5 throws is {total}')


#%%
seed(1234)

die = [randint(1, 6) for i in range(5)]

total = sum(die)

print(f'The total of 5 throws is {total}')

