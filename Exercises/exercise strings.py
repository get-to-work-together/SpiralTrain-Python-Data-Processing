#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:30:16 2022

@author: peter
"""

s = input('Give me some text: ')

print('the text:',                  s)
print('upper:',                     s.upper())
print('lower:',                     s.lower())
print('capitalize:',                s.capitalize())
print('title:',                     s.title())
print('first 3 characters:',        s[:3])
print('ends with a question mark:', s.endswith('?'))
print('snake case:',                s.lower().replace(' ', '_'))



