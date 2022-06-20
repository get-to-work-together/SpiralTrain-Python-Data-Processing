import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('classic')


# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(1, 2, sharex = True, figsize = (10, 8))

fig.suptitle('Two signals', fontsize=16)

axs[0].scatter(s1, s2, 
               marker = 's', 
               s = 80,
               color = 'orange', 
               facecolor=(0, 0.5, 0.5, 0.1), 
               edgecolor='darkkhaki')
axs[0].set_xlabel('s1')
axs[0].set_ylabel('s2')
axs[0].grid()

# axs[0].plot(t, s1)
# axs[0].set_xlim(0, 2)
# axs[0].set_ylim(-10, 10)
# axs[0].set_ylabel('s1')
# axs[0].grid(True)

axs[1].set_xlim(0,1)
axs[1].plot(t, s1)
axs[1].plot(t, s1+2)
axs[1].plot(t, s1+4)
axs[1].plot(t, s1+6)
axs[1].plot(t, s1+8)
axs[1].plot(t, s1+10)
# axs[1].plot(t, 3*s1)
# axs[1].plot(t, 4*s1)
# axs[1].plot(t, 5*s1)
# axs[1].plot(t, 6*s1)

# axs[1].plot(t, s2)
# axs[1].set_xlim(0, 2)
# axs[1].set_ylim(-10, 10)
# axs[1].set_xlabel('time')
# axs[1].set_ylabel('s2')
# axs[1].grid(True)

axs[1].annotate('important', xy=(0.5, 12.4), xytext=(0.5, 14), arrowprops={'arrowstyle':'->'})


fig.tight_layout()

plt.savefig('plot1.png')

plt.show()

