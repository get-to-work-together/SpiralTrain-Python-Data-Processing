#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:29:33 2022

@author: peter
"""

import math

r = float(input('What is the radius of your circle?\n'))

area = math.pi * r ** 2
circumference = 2 * math.pi * r

print('Circle')
print('  radius', r)
print('  area', round(area, 3))
print('  circumference', round(circumference, 3))

#%% or

print('Circle')
print(f'  radius        : {r:8.3f}')
print(f'  area          : {area:8.3f}')
print(f'  circumference : {circumference:8.3f}')

