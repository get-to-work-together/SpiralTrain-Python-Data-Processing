#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:36:16 2022

@author: peter
"""

import math

#%%

class Vector:
    """This is my beutiful Vector class"""

    __slots__ = ['_force','_direction']
    
    
    def __init__(self, f, d):
        """Initialization.
        f - force
        d = direction [radians]"""
        self._force = f
        self._direction = round(d, 12)   # in radians
        
    @property
    def direction(self):
        return self._direction

    @property
    def force(self):
        return self._force

    @property
    def x(self):
        return self._force * math.cos(self._direction)
    
    @property
    def y(self):
        return self._force * math.sin(self._direction)
    
    def __repr__(self):
        return f"Vector({self._force}, {self._direction})"
    
    def __add__(self, other):
        return Vector.add(self, other)

    @classmethod
    def add(cls, v1, v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        f = math.sqrt(x ** 2 + y ** 2)
        d = math.atan2(y, x)
        return cls(f, d)
    
    def is_parallel(self, other):
        return Vector.is_parallel_static(self, other)

    @staticmethod
    def is_parallel_static(v1, v2):
        return math.isclose(v1.direction, v2.direction) or \
            math.isclose(v1.direction, math.pi + v2.direction)
        
    
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        

    