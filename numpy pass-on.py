#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:47:14 2022

@author: peter
"""

import numpy as np

#%%
# numpy array 3 x 20 with random numbers netween 1 and 100

a = np.random.randint(1, 100, size = (3, 20))
print(a)

#%%
# take the sin square of each element

np.sin(a) ** 2

def f(x):
    return np.sin(x) ** 2

a = f(a)

print(a)

#%%
# find find all indeces of elements with values > 0.3 and <= 0.9
# all elements outside this range set to 0

indeces = (a > 0.3) & (a <= 0.9)
indeces

a[np.invert(indeces)] = 0
a

#%%
# second array with with x and poly fit on x, y

x = np.arange(a.shape[1])

from numpy.polynomial import Polynomial as P

p = P.fit(x, a[0], 5)

import matplotlib.pyplot as plt

plt.plot(x, a[0], 'o')

plt.plot(x, p(x), 'r')

plt.show()

