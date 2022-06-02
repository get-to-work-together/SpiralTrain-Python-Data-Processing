#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

#%%

m1 = np.array( [[0, 1], 
                [1, 0]] )

m2 = np.array( [[4, 1], 
                [2, 2]] )

print( np.dot(m1, m2) )

#%%

v1 = np.array( [1, 2, 3] )
v2 = np.array( [0, 1, 1] )

print( np.inner(v1, v2) )

#%%

v1 = np.array( [1, 2, 3] )
v2 = np.array( [0, 1, 2] )

print( np.outer(v1, v2) )

#%%

m1 = np.array([[1, 0],
               [0, 1]])

m2 = np.array([[4, 1],
               [2, 2]])

print( np.matmul(m1, m2) )

print( m1 @ m2 )

#%%

v1 = np.array([2j, 3j])
v2 = np.array([2j, 3j])

v1 @ v2
