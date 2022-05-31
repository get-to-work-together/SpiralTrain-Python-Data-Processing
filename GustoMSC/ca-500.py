#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:56:21 2022

@author: peter
"""

import pandas as pd

#%%

filename = 'ca-500.csv'

df = pd.read_csv(filename, sep = ',')
df

#%%

columns_of_interest = ['first_name','last_name','city','email']

selected = df.loc[(df['city']=='Montreal') | (df['city']=='Toronto') , columns_of_interest]
selected = df.loc[df['city'].isin(('Montreal','Toronto')) , columns_of_interest]

selected

#%%

columns_of_interest = ['first_name','last_name','city','email']

selected = df.loc[df['email'].str.endswith('hotmail.com') , columns_of_interest]

selected

#%%


s = df['province'].value_counts()
s.plot(kind = 'barh')


