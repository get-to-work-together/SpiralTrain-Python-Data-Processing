# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

numbers = list(range(20))

squares = [number ** 2 for number in numbers]
print(squares)

squares = []
for number in numbers:
    squares.append(number ** 2)


#%%

squares = [number ** 2 for number in numbers if number % 2 == 0]
print(squares)


#%%

multiplication = [[i * j for i in range(5)] for j in range(10)]
print(multiplication)


#%%

d = {number: number ** 2 for number in numbers}
print(d)

#%%

g = (number ** 2 for number in numbers)
print(g)

#%%

import random
random.shuffle(numbers)

print(numbers)


def distance_to_10(number):
    return abs(10 - number)


print(sorted(numbers, key = distance_to_10))


#%%

sentence = 'Today is monday and the Coffe is good'
words = sentence.split()

def reverse(word):
    return ''.join(reversed(word))

sorted(words, key = reverse)

#%%

print( sorted(words, key = lambda word: word[::-1]) )

#%%

sorted(words, key = str.lower)

sorted(words, key = lambda w: w.lower())

#%%

#list(filter(lambda word: len(word) > 3 , words))

list(filter(lambda word: 'o' in word , words))


def has_o(word):
    return 'o' in word

list(filter(has_o , words))

[word for word in words if 'o' in word]


#%%

list(map(lambda word: word.upper()[:4] , words))

[word.upper()[:4] for word in words]

