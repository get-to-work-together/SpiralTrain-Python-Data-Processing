# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:53:48 2022

@author: peter
"""

from material import Material
from node import Node

class Beam:
    
    def __init__(self, length = 0, material = None):
        self._length = length
        self._material = material
        self._nodes = []
        
    def __str__(self):
        return f'Beam({self._length}, {self._material})'
    
    # setters and getters
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if length < 0:
            raise Exception('Dimensions can only be positive.')
        self._length = length
        
    def info_nodes(self):
        s = ''
        for node in self._nodes:
            s += str(node) + '\n'
        return s
    
    def add_node(self, node):
        self._nodes.append(node)
        
    def distribute_nodes(self, number_of_nodes):
        d = self._length / (number_of_nodes - 1)
        for node_nr in range(number_of_nodes):
            node = Node(node_nr, round(node_nr * d, 10))
            self._nodes.append(node)

#------------------------------------------------
    
if __name__ == '__main__':
    
    m1 = Material('steel', 2.1e11)
    
    beam = Beam(1.2, m1)

    beam.length = -2.0
    
    print(beam.length)
    
    print(beam)
    
    beam.distribute_nodes(5)
    
    print(beam.info_nodes())
