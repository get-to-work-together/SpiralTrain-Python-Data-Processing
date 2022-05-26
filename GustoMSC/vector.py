# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:22:39 2022

@author: peter
"""

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return print('This is really strange operation')
    
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __abs__(self):
        return self.length()
    
    
#-----------------------------------

if __name__ == '__main__':
    
    v1 = Vector(3, 4)
    v2 = Vector(3, -2)
    
    print(v1)
    print(v2)
    
    v3 = v1 + v2
    
    print(v3)
    
    v1 - v2