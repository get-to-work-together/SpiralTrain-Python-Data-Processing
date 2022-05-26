# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:53:21 2022

@author: peter
"""

#%%

def print_goodmorning():
    print('Goodmorning')
    print('How are you today?')
    print('Have a great day!')


print_goodmorning()


#%%

def print_goodmorning(name):
    print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


print_goodmorning('Peter')

#%%

def print_goodmorning(name = 'Stranger'):
    print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


print_goodmorning()

print_goodmorning(name = 'Steven')


#%%

numbers = [2,3,5,6,7]
a,b,c,*_ = numbers


#%%
def maximum(*numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

print(maximum(2,3,5,8))

list_of_numbers = [2,3,5,6,7]
print(maximum(*list_of_numbers))

#%%

def f(*args, **kwargs):
    print(args)
    for arg in args:
        print(arg)
    print(kwargs)
    for name, value in kwargs.items():
        print(name, value)
        
f(5,2,8,'abc', factor = 2, x = 0.6)

settings = {'factor': 5, 'x':0.9}
f(**settings)




#%%

def calc(n1, n2):
    return n1 + n2, n1 - n2

s, d = calc(2, 4)
print( d )

#%%

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def do_it(n1, n2, f):
    return f(n1, n2)


print( do_it(3, 6, add)  )
print( do_it(3, 6, subtract)  )
print( do_it(3, 6, multiply)  )

print( do_it(3, 6, max)  )

#%%

words = 'This is a LOT of rubish and bla blAAAAAAAa'.split()

print(  sorted(words)  )

print(  sorted(words, key = len)  )

def number_of_a(word):
    return word.count('a')

print(  sorted(words, key = number_of_a)  )

print(  sorted(words, key = str.lower)  )

print(  sorted(words, key = lambda word: word.lower().count('e'))  )

#%%


def number_of_characters(word, c):
    return word.lower().count(c)

def number_of_a(word):
    return number_of_characters(word, 'a')

#%%

def say():
    greeting = 'Hello Goodbye'

    def display():
        print(greeting)

    return display 


f = say()

f()

#%%

n = 0
def f(x, y):
    global n
    n += 1
    z = x**2 + y**2 + n
    return z

print( f(4,5) )

#%%

numbers = [3,6,4,8,9,3,4,6]

print( sorted(numbers, key = lambda x: 1/x) )

print( list(filter(lambda x: x > 4, numbers)))

print( list(map(lambda x: x > 4, numbers)))
print( list(map(lambda x: 1/x, numbers)))

print([1/x for x in numbers if x > 4])



