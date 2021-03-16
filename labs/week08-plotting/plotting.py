#plotting.py
#Author: Andrew Beatty

import matplotlib.pyplot as plt #imports matplotlib module renameit as "plt"

import numpy as np #imports numpy module as "np"
'''
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself
matplotlib.pyplot.plot(xpoints, ypoints)  #could say matplotlib.pyplot.plot(xpoints, ypoints)
#and remove as plt but "plt" shorter
matplotlib.pyplot.show()
'''

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself
plt.plot(xpoints, ypoints)  #could say matplotlib.pyplot.plot(xpoints, ypoints)  "plt" shorter
plt.show()


