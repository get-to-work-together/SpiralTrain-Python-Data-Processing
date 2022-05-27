# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:43:59 2022

@author: peter
"""

from finite_elements.beam import Beam
from finite_elements.material import Material

beam = Beam(1, Material('wood', 1.9e20))

print(beam)