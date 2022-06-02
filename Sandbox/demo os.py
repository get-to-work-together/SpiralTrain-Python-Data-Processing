#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:33:53 2022

@author: peter
"""

import os

#%%
# Current working directory
print(os.getcwd())

#%%
# Directory contents
print(os.listdir('.'))

for entry in sorted(os.listdir('.')):
    print(entry)
    
#%%
# Paths in windows
path = 'C:\\temp'
path = r'C:\temp'
os.path.join('C:', 'temp')
path = 'C:/temp'

