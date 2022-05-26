# -*- coding: utf-8 -*-
"""
Created on Mon May 23 12:46:21 2022

@author: peter
"""

import math

r = 3

circumference = 2 * r * math.pi

print('The circumference is ' + str(circumference))

print('The circumference is %.3f' % circumference)

print('The circumference is {:.3f}'.format(circumference))

print(f'The circumference is {circumference:.3f}')

