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

xnew = np.linspace(0, 10, num=81, endpoint=True)

plt.plot(x, y, 'o', 
         xnew, f1(xnew), '-', 
         xnew, f2(xnew), '--', 
         xnew, f3(xnew), '--')
plt.legend(['data', 'linear', 'quadratic',  'cubic'], loc='best')
plt.show()

