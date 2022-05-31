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

a = np.linspace(1, 10, 20)
print(a)

#%%
a = np.ones(10)
a

#%%
a = np.ones(shape = (5, 3), dtype = 'int64')

print (a.shape)
print (a.dtype)
print(a)

#%%

m = np.arange(1, 17).reshape(8, 2)
print(m)

print(m.ndim)
print(m.shape)

#%%

print(m[0])

#%%

np.append(m, [17, 18])

np.append(m, [17, 18], axis = 0)

v = np.arange(1, 9).reshape(8,1)
np.vstack([m, v])

#%%

np.sort(v)
np.argsort(v)
indeces = np.argsort(v)
v[indeces]

#%%
np.max(v)
np.argmax(v)
np.min(v)
np.argmin(v)

#$$
indeces = np.where(v == 7)
v[indeces]


#%%

np.save('data.npy', m)

del m

m = np.load('data.npy')

#%%

import pickle

with open('data.pickle', 'wb') as f: pickle.dump(m, f)

del m

with open('data.pickle', 'rb') as f: m = pickle.load(f)



