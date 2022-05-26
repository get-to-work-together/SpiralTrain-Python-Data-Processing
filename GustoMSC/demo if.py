# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:42:16 2022

@author: peter
"""

gender = 'M'
age = 15

if gender.lower() == 'm':
    if age < 21:
        print('boy')
    else:
        print('man')
elif gender == 'f':
    if age < 21:
        print('girl')
    else:
        print('woman')
else:
    print('other')


counter = 0
while counter < 10:
    print(counter)
    counter += 1
    
counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

#%%
for number in range(1, 10):
    if number == 7:
        continue
    print(number)
    
#%%
while True:
    number = int(input('Enter an number between 1 and 10: '))

    if 1 <= number <= 10:
        break


#%%

p = 't:\\packages'
import sys
sys.path.append(p)

import os
for d in os.listdir('C:\\Users'):
    sys.path.append(d)


