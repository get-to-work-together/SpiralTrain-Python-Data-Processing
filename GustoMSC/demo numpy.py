# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:30:41 2022

@author: peter
"""

import numpy as np

#%%

numbers = [1,2,3,4,5,6,7,8]
print(numbers)

a = np.array(numbers)
print(a)

#%%

a = np.arange(1, 10, 0.5)
print(a)

#%%

a = np.linspace(1, 10, 19, endpoint=True)
print(a)

#%%

m = np.arange(1, 17).reshape(8, 2)
print(m)

print(m.ndim)
print(m.shape)

#%%

print(m[0])

#%%

print(a)













