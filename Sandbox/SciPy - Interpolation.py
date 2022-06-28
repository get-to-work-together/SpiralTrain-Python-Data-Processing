#!/usr/bin/env python
# coding: utf-8

# In[5]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# In[10]:

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x ** 2 / 9.0)

f1 = interp1d(x, y)
f2 = interp1d(x, y, kind='quadratic')
f3 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=101, endpoint=True)

plt.plot(x, y, 'o', 
         xnew, f1(xnew), '-', 
         xnew, f2(xnew), '--', 
         xnew, f3(xnew), '--')
plt.legend(['data', 'linear', 'quadratic',  'cubic'], loc='best')
plt.axhline(1.0, lw=1, c='lightgray', zorder = 0)
plt.axhline(-1.0, lw=1, c='lightgray', zorder = 0)
plt.show()

#%%

from scipy.optimize import curve_fit

def model(x, a, b):
    return np.cos(-x ** a / b)
    
p0 = (1.7, 7)
fitted = curve_fit(model, x, y, 
                   p0 = p0,
                   bounds = ((0, 1), (np.inf, np.inf)),
                   method = 'dogbox')

popt, _ = fitted
print(f'Coefficients: {popt}')

plt.plot(x, y, 'o', 
         xnew, model(xnew, 2.0, 9.0), '-',
         xnew, model(xnew, *popt), '--',
         xnew, model(xnew, *p0), '.', ms=1)
plt.legend(['data', 'original', 'fitted'], loc='best')
plt.axhline(1.0, lw=1, c='lightgray', zorder = 0)
plt.axhline(-1.0, lw=1, c='lightgray', zorder = 0)
plt.show()