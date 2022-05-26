# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:02:33 2022

@author: peter
"""

def count_calling(f):
    count = 0
    
    def wrapper(*args, **kwargs):
        count += 1
        return f(*args, **kwargs)

    return wrapper
    

@count_calling
def do_something():
    print('yeah')
    

do_something()