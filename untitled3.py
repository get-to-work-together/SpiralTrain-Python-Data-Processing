#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:25:22 2022

@author: peter
"""

import pandas as pd

#%%

sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df = pd.DataFrame(sales)

#%%
# Exploration

df.info()

print( df.columns )
print( df.index )


#%%

df
df.head(10)
df.tail(10)

#%%
# Selecting a column

col = df['account']
print( type(col) )
print( col )
print( col.dtype )

col = df['Jan']
print( type(col) )
print( col )
print( col.dtype )

#%%
# Selecting multiple columns

df2 = df[['account','Jan']]
print( type(df2) )
print( df2 )

#%%
# Filter a row

print( df[df['account']=='Alpha Co'] )



