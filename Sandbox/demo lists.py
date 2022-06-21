#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:50:37 2022

@author: peter
"""

shopping_list = ['milk','eggs','butter']

print(shopping_list)
print(type(shopping_list))

#%%

shopping_list.append('bread')
print(shopping_list)

shopping_list.insert(0, 'beer')
print(shopping_list)

#%%

shopping_list.pop()
print(shopping_list)

shopping_list.pop(0)
print(shopping_list)

#%%

shopping_list.sort()
print(shopping_list)
