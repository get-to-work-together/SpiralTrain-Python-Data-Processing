# This is comment

name = 'Peter'

print('Hello ' + name)

#%%

print('This is the second cell')

#%%

print('This is the third cell')


#%%

name = input('What is your name? ')

print('Hello ' + name)

#%%

# PEP8 - coding style

number_of_cars = 6              # YES - snake case

n = 9                           # NO

numbersOfCars = 9               # NO - camelCase

NumberOfCars = 9                # Only for class names - Pascal case

intNumberOfCars = 9

NUMBER_OF_CARS = 9              # Only for constants - SCREAMING_CASE

#%%

import sys

print(sys.name)

#%%

from math import pi

print(pi)


#%% Docstring

"""This is documentation. Using triple quotes.

Multiple lines are OK!"""

#%% Keywords

#%% Numeric

number = 320007987878678968768768768768768768768768768768768767867868
print(type(number))

print(number + 1)


x1 = 0.1
x2 = 0.2

print(x1 + x1)
print(x2 + x2)
print(x1 + x2)

print(x1 + x2 == 0.3)

#%% Decimal

from decimal import Decimal

d1 = Decimal('0.1')
d2 = Decimal('0.2')

d3 = d1 + d2

print(d3)

#%% math

import math

print(math.pi)
print(math.sin(math.pi * 0.5))


from math import pi
print(pi)

import math as m
print(m.pi)







