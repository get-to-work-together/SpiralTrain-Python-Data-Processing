import numpy as np
import matplotlib.pyplot as plt

#%%

def model(x):
    a = 2
    b = 5
    return a * x + b

#%%

x_model = np.linspace(0, 80)
y_model = model(x_model)

#%%

plt.plot(x_model, y_model)

#%%

n = 100

x_data = np.random.uniform(0, 80, n)

spread = 30

noise = np.random.randn(n) * spread

y_data = model(x_data) + noise

#%%

plt.scatter(x_data, y_data)

#%%

coefs = np.polyfit(x_data, y_data, 1)

print(coefs)

#%%

regression = np.poly1d(coefs)

plt.plot(x_model, y_model, color = 'green')
plt.scatter(x_data, y_data)
plt.plot(x_model, regression(x_model), color = 'red')

plt.show()



