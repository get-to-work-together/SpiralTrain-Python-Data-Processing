#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:53:10 2022

@author: peter
"""



def calculate_area1(width, height):
    if width < 0 or height < 0:
        raise Exception('Width or height can not be negative')
    return width * height


def calculate_area2(width, height):
    assert width >= 0 and height >= 0, 'Width or height can not be negative'
    return width * height




print(calculate_area2(4, -4))