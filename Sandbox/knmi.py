#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:46:44 2022

@author: peter
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

stations = {
    260: 'De Bilt',
    279: 'Hoogeveen'
}


#%%
# Read files

filename_260 = 'etmgeg_260.txt'
filename_279 = 'etmgeg_279.txt'

df_260 = pd.read_csv(filename_260, 
                     skiprows = 50, 
                     parse_dates = [1],
                     low_memory = False)

df_279 = pd.read_csv(filename_279, 
                     skiprows = 50, 
                     parse_dates = [1],
                     low_memory = False)
    

#%%
# Fix column names

df_260.columns = [colname.strip() for colname in df_260.columns]
df_260.rename(columns = {'# STN':'STN'}, inplace = True)

df_279.columns = [colname.strip() for colname in df_279.columns]
df_279.rename(columns = {'# STN':'STN'}, inplace = True)


#%%
# Filter rows and select columns

year = 2021
columns = ['STN', 'YYYYMMDD', 'TG']

df_260 = df_260.loc[df_260['YYYYMMDD'].dt.year == year, columns]
df_279 = df_279.loc[df_279['YYYYMMDD'].dt.year == year, columns]


#%%
# Convert date

df_260['DD'] = pd.to_datetime(df_260['YYYYMMDD'], format = '%Y%m%d')
df_279['DD'] = pd.to_datetime(df_279['YYYYMMDD'], format = '%Y%m%d')


#%%
# Merge into one dataframe

df = pd.concat([df_260, df_279])


#%%
# Convert temperature

df['TG'] = df['TG'].astype('float') / 10


#%%
# Convert station

stations = {
    260: 'De Bilt',
    279: 'Hoogeveen'
}

df['STATION'] = df['STN'].map(stations)


#%%

daily_temperature = df.reset_index().set_index(['DD','STATION'])['TG'].unstack()


#%%

daily_temperature.plot(kind = 'line', title = 'Daily')

#%%

weekly_temperature = daily_temperature.resample('W').mean()
weekly_temperature.plot(kind = 'line', title = 'Weekly')
 
#%%
 
daily_temperature.resample('M').mean().plot(kind = 'line', title = 'Monthly')

#%%
# Calcilate and plot differences

diff = daily_temperature['Hoogeveen'] - daily_temperature['De Bilt']

diff.plot.line()

plt.axhline(0, c = 'r', lw = 3, zorder = 10)
plt.grid()

#%%

diff.plot.hist(bins = 20)
diff.plot.kde(secondary_y=True)

#plt.axvline(0, c = 'r', lw = 3, zorder = 0)
plt.grid()

#%%
#

n_kouder = np.sum(diff < 0)
n_totaal = diff.shape[0]

print('Op %d van de %d dagen (%.0f%%) is het kouder in %s dan in %s' % (n_kouder, 
                                                                        n_totaal, 
                                                                        100*n_kouder/n_totaal, 
                                                                        'Hoogeveen', 
                                                                   'De Bilt'))


#%%

mean_diff = np.mean(diff)

print(f'Gemiddeld is het {-mean_diff:.1f} graden kouder')

#%%

from scipy import stats
t, p = stats.ttest_1samp(diff, 0)

print("The t-statistic is %.3f and the p-value is %.5f." % (t, p/2))



