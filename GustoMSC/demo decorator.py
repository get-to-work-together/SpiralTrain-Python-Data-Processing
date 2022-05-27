# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:02:33 2022

@author: peter
"""

def count_calling(func):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'This function has now been called {count} time{"" if count==1 else "s"}.')
        return func(*args, **kwargs)

    return wrapper
    

@count_calling
def do_something():
    print('Yeah')
    
#----------------------------------------------------------------

do_something()
do_something()
do_something()
do_something()

