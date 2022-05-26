# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:53:56 2022

@author: peter
"""

class Node:
    
    def __init__(self, node_nr, x):
        self._node_nr = node_nr
        self._x = x
        
    def __str__(self):
        return f'Node({self._node_nr}, {self._x})'
    
#-------------------------------------------------------
    
if __name__ == '__main__':
    
    node = Node(1, 0)
    
    print(node)