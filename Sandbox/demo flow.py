#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:53:43 2022

@author: peter
"""

gender = 'm'
age = 34

if gender == 'm':
    if age < 21:
        print('boy')
    else:
        print('man')
elif gender == 'v':
    if age < 21:
        print('girl')
    else:
        print('woman')
else:
    print('other')
    
#%%

gender = 'f'

if gender == 'm':
    print('male')
    
else:
    print('female')
    print('done')
    
#%%

answer = ''
while answer != 'x':
    answer = input('Stop by typing x: ')

#%%

while True:
    answer = input('Stop by typing x: ')
    if answer == 'x':
        break

#%%

while True:
    number = int(input('Enter an number between 1 and 10: '))

    if 1 <= number <= 10:
        break

print(number)
    
    
    
    
    
    