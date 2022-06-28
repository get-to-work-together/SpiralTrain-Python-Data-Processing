#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:04:41 2022

@author: peter
"""

import math

class Vector:
    """This is my Vector class"""
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __repr__(self):
        return f'[{self._x }, {self._y}]'
    
    @property
    def amplitude(self):
        """Pythagoras"""
        return (self._x ** 2 + self._y ** 2) ** 0.5
    
    @property
    def angle(self):
        """Trigiometry"""
        return math.atan2(self._y, self._x)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __lt__(self, other):
        return self.amplitude < other.amplitude
    def __le__(self, other):
        return self.amplitude <= other.amplitude
    def __gt__(self, other):
        return self.amplitude > other.amplitude
    def __ge__(self, other):
        return self.amplitude >= other.amplitude
    def __eq__(self, other):
        return self.amplitude == other.amplitude
    def __ne__(self, other):
        return self.amplitude != other.amplitude
 

class Trajectory:
    
    def __init__(self):
        self.vectors = []
        
    def append(self, v):
        self.vectors.append(v)
        
    @property
    def length(self):
        return sum(v.amplitude for v in self.vectors)
    
    
if __name__ == '__main__':
    
    v1 = Vector(3, 4)
    v2 = Vector(-2, 5)
    
    print(v1)
    print(v2)
    
    v3 = v1 + v2
    
    print(v3)
    
    t = Trajectory()
    t.append(v1)
    t.append(v2)
    t.append(v3)
    print(t.length)
    
    