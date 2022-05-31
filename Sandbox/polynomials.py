import numpy as np

from numpy.polynomial import Polynomial as P

import matplotlib.pyplot as plt

np.polynomial.set_default_printstyle('unicode')

#%%
def plot(p):
    x = np.linspace(-10, 10, 101)
    plt.axhline(0, c='k', lw=1)
    plt.axvline(0, c='k', lw=1)
    plt.plot(x, p(x), c='r', lw = 3)
    plt.grid()
    plt.show()

#%%
p = P([-3, 2, 1])

print( p.coef )
print( p )
print( p.roots() )

plot(p)

#%%
print( 'addition:', p + p )
print( 'multiplication:', 10 * p )
print( 'power:', p ** 2 )

print( 'substitution:', p(p) )

#%%

p = P.fromroots([-5, 0, 5])
plot(p)
print(p)

#%%
#
# Calculus: integration and differentiation

p = P([1, 2, 3])
print( p )

print( 'differentiation:', p.deriv() )

print( 'integration:', p.integ() )

#%%
#
# Fitting

np.random.seed(11)

x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x) + np.random.normal(scale=.4, 
                                 size=x.shape)

plt.plot(x, y, 'o')
plt.show()


#%%
#
# Fitting

p = P.fit(x, y, 5)

plt.plot(x, y, 'o')
xx, yy = p.linspace()

plt.plot(xx, yy, lw=2)
plt.show()

print(p)

print( 'domain:', p.domain )
print( 'window:', p.window )

#%%

from numpy.polynomial import Chebyshev


p = Chebyshev.fit(x, y, 5)

plt.plot(x, y, 'o')
xx, yy = p.linspace()

plt.plot(xx, yy, lw=2)
plt.show()

print(p)

print( 'domain:', p.domain )
print( 'window:', p.window )




