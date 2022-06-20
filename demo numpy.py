import numpy as np

#%%

numbers = [3,6,8,2,9,4]
print(numbers)
print(type(numbers))

a = np.array(numbers)
print(a)
print(type(a))


#%%

a = np.arange(1, 11, 0.5)
print(a)

#%%

a = np.linspace(1, 11, 41)
print(a)

#%%

a = np.zeros(20)
print(a)

a = np.ones(20)
print(a)

a = np.full(20, 9.)
print(a)

#%%

print(a.ndim)
print(a.shape)


#%%

a = np.zeros((10, 2))
print(a)
print(a.ndim)
print(a.shape)

#%%

a = np.zeros((2, 10))
print(a)
print(a.ndim)
print(a.shape)

#%%

print(a.T)
print(a.transpose())

a = a.transpose()

#%%

a = np.arange(1, 21).reshape((2, 10))
print(a)
print(a.ndim)
print(a.shape)

#%%

a = a.reshape((5, 4))
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)


#%%

a = np.array([1,2,3,4,5,6.2,7,8,9])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

#%%

a = np.zeros((2, 10), dtype = np.int32)
print(a)
print(a.ndim)
print(a.shape)

#%%

a = np.arange(1, 21).reshape((4, 5), order = 'C')
print(a)
print(a.ndim)
print(a.shape)

#%%

a = np.arange(1, 21).reshape((4, 5), order = 'F')
print(a)
print(a.ndim)
print(a.shape)

#%%

a = np.zeros(10)
for number_of_rows in range(3):
    a = np.vstack((a, np.ones(10)))
    
print(a)
print(a.ndim)
print(a.shape)    
    
print(np.hstack((a, np.arange(1, 5).reshape(4,1))))

#%%

a = np.identity(6)
print(a)


#%%

a = np.diag(np.arange(1, 6))
print(a)

print(a.diagonal())


#%%

print( a.ravel() )


#%%

a = np.arange(3, 13)
print(a)

print(a[0])
print(a[1])
print(a[-1])
print(a[3:7])

#%%

a = np.arange(1, 21).reshape(4, 5)
print(a)

print(a[0])
print(a[-1])

print(a[0][3])
print(a[0, 3])

print(a[0:3, 3])
print(a[:, 4])

print(a[2:4, 2:4])

#%%

a = np.arange(1, 21)

print( a[ [5,2,9,10] ] )

print( a[ [5,2,9,10] ] )

#%%

a = np.arange(1, 21)
print( a + 100 )


#%%

a = np.arange(1, 21)

print( a % 3 == 0 )
print( a[a % 3 == 0] )

print( (a % 3 == 0) | (a % 4 == 0) )
print( a[(a % 3 == 0) | (a % 4 == 0)] )

#%%

c = np.arange(1, 31).reshape(3, 2, 5)
print(c)


print( c[2, :, 1:3])

#%%

a = np.arange(1, 22).reshape(3, 7)

print(a)

print(a + 100)

print(a + a)

b = np.arange(1, 8)

print(b)
print(a + b)

print((a.T + np.array([100, 200, 300])).T)

#%%

x = np.linspace(0, 10, 101)
y1 = np.sin(x)
y2 = np.cos(x) / (x + 1)

import matplotlib.pyplot as plt

plt.axhline(0, color = 'black', linewidth = 1)
plt.grid()
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

#%%

print(y1 + y2)

print(np.add(y1, y2))

#%%

a = np.array([34,76,98,34,78,21,23])

print(a)

a.sort()

print(a)
print(np.sort(a))

print(a)

#%%

a = np.array([34,76,98,34,78,21,23])

indeces = np.argsort(a)

print(indeces)

print(a[indeces])

#%%

a = np.array([34,76,98,34,78,21,23])

print(a)

indeces = np.where(a>50)

print(indeces)

#%%

a = np.array([34,76,98,34,78,21,23])

np.save('data_out.npy', a)

b = np.load('data_out.npy')

print(a)
print(b)





 

