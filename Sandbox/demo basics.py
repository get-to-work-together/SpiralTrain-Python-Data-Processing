#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:42:32 2022

@author: peter
"""

#%%
# Variables

name = 'Peter'
print(name)
print(type(name))

number_of_cars = 10   # Python PEP8



#%%
# Numerical

# integer
i = 79879879879
print(i)

# float
f1 = 0.1
f2 = 0.2

print(f1 + f1)
print(f2 + f2)
print(f1 + f2)

print(f1 + f1 == 0.2)
print(f1 + f2 == 0.3)

print(round(f1 + f2, 10))

# complex
c1 = (5 + 3j)
print(c1)
print(type(c1))
print((0 + 1j) ** 2)

#%%
# Decimal

from decimal import Decimal

d1 = Decimal('0.1')
d2 = Decimal('0.2')

print(d1 + d2)
print(float(d1 + d2) == 0.3)


#%%
# Operators

n1 = 56
n2 = 8

print( 'addition',          n1 + n2   )
print( 'subtraction',       n1 - n2   )
print( 'multiplication',    n1 * n2   )
print( 'division',          n1 / n2   )
print( 'floored division',  n1 // n2   )
print( 'modulo',            n1 % n2   )
print( 'power',             n1 ** n2   )

print('divmod',             divmod(27, 6) )

#%%
# String

s1 = 'abc'
s2 = "def"

print(s1)
print(s2)

print( "Say 'hello'" )
print( 'Say "hello"' )

print( 'Say \'hello\'' )

print( '''\
line 1
line 2
line 3''' )


#%%
# concatenate
print( s1 + s2 )

temperature = 20
#print( 'Temperature is ' + temperature )
print( 'Temperature is ' + str(temperature) )
print( 'Temperature is', temperature )

print( s1 + s1 )
print( 10 * s1 )

#%%
# string formating

print(  f'Temperature is {temperature}'   )
print(  'Temperature is %d' % temperature   )
print(  'Temperature is {}'.format(temperature)   )

import math

print(  f'Pi is {math.pi}')
print(  f'Pi is {math.pi:.4f}')
print(  f'Pi is {math.pi:10.4f}')

print(  f'Temperature is >{temperature:20}<'   )
print(  f'Temperature is >{temperature:<20}<'   )
print(  f'Temperature is >{temperature:^20}<'   )

#%%
# String methods

text = 'A monkey climbs in a  tree'

print( 'text',         text     )

print( 'upper',        text.upper()      )
print( 'lower',        text.lower()      )
print( 'capitalize',   text.capitalize()      )
print( 'title',        text.title()      )

print( 'count',        text.count('e')      )

print( 'endswith',     text.endswith('e')      )
print( 'startswith',   text.startswith('e')      )

print( 'find',         text.find('e')      )
print( 'index',        text.index('e')      )

words = text.split() 
print( 'split',        words )
print( 'join',         '-'.join(words))

print( 'replace',      text.replace('monkey', 'dog') )
print( 'translate',    text.translate(str.maketrans('aeiou', 'AEIOU', 'mn')) )

print( 'chaining',     text.replace('monkey', 
                                    'dog')
                           .replace('tree', 
                                    'bush') )

print( 'in',  'tree' in text )

#%%
# Indexing and slicing

text = 'abcdefghijklm'

print( text[0] )    # zero based
print( text[6] )

print( text[-1] )
print( text[-2] )

print( text[3:6] )
print( text[-3:] )
print( text[:5] )

#%%
# Input

name = input('What is your name? ')

print('Hello ' + name)

age = int(input('How old are you? '))

print(f'Next year you will be {age + 1}')


#%%
# Math

import math

print(math.pi)

r = float(input('Give me the radius of a circle: '))

area = math.pi * r**2
print(f'The area is {area:.3f}')

#%%
# Random

import random

random.seed(1234)

secret_number = random.randint(1, 100)

print(secret_number)

print(   random.random()  )

print([random.randint(1, 100) for _ in range(20)])

#%%
# Conditional

n1 = 45
n2 = 78

n = 56

print(n1, n2, n)

print('==',   n1 == n2  )
print('!=',   n1 != n2  )
print('>',    n1 > n2  )
print('>=',   n1 >= n2  )
print('<',    n1 < n2  )
print('<=',   n1 <= n2  )

print('< and >',    (n > n1) and (n < n2))
print('< or >',     (n < n1) or  (n > n2))

print('between < <',    n1 < n < n2)

is_larger = n > n1
is_smaller = n < n2

in_between = is_larger and is_smaller

#%% 
# Lists

numbers = [1, 2, 6, 3, 7, 9, 3, 4]
print(numbers)

print( 8 in numbers )
print( 9 in numbers )

print( 'tree' in text )




