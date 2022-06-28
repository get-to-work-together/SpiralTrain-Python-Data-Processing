#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:37:20 2022

@author: peter
"""

filename = 'dataX.csv'
outfile = 'data.out'

try:
    with open(filename, encoding = 'utf-8') as f:
        
        with open(outfile, mode = 'w') as f_out:
        
            header_line = f.readline().strip()
            header = header_line.split(';')
            
            for line in f:
                line = line.strip()   
                values = line.split(';')
                
                d = dict(zip(header, values))
                
                if 'EQ' in d['Department']:        
                    s = f'{d["ID"]:3} {d["Name"]:10} ({d["Department"]}) => {d["Points"]}'
                    print(s)
                    
                    f_out.write(s + '\n')

# or                
#                print(s, file = f_out)

except FileNotFoundError:
    print(f'Cannot open file {filename}')
    
    
