#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:02:30 2022

@author: peter
"""

import numpy as np

#%%

numbers = np.arange(1, 20, 0.5)
print(numbers)


print('type', type(numbers))

print('ndim', numbers.ndim)
print('shape', numbers.shape)
print('len', len(numbers))

print('dtype', numbers.dtype)


#%%


print(numbers.min())
print(numbers.max())
print(numbers.mean())
print(numbers.sum())
print(numbers.std())


#%%

numbers = np.arange(1, 21)
print(numbers)

m = numbers.reshape( (5, 4), order = 'C' )

print(m)
print(m.ndim)
print(m.shape)

print(m.transpose)
print(m.T)

#%%

[numbers ** 2 for number in numbers]


