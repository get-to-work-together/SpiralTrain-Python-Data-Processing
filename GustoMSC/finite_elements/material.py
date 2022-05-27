# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:54:13 2022

@author: peter
"""


class Material:
    """Material class
    
    Attributes:
        type
        E_modulus (in N/m2)
    """
    
    def __init__(self, material_type, E_modulus):
        self._material_type = material_type
        self._E_modulus = E_modulus
        
    def __str__(self):
        return f'Material("{self._material_type}", "{self._E_modulus:.3e}")'
 
#-----------------------------------------------------------
    
if __name__ == '__main__':
    
    material = Material('steel', 2.1e11)
    
    print(material)
        