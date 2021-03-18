#plottask.py
#Author: PaulMcGrath
# displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# in a nice looking plot

import matplotlib.pyplot as plt #imports matplotlib module renameit as "plt"

import numpy as np #imports numpy module as "np"

xpoints = np.array(range(0,5))
ypoints = xpoints  #multiply each entry by itself

#xpoints = np.array(range(0,5))
ypoints2 = xpoints * xpoints #multiply each entry by itself squared

#xpoints = np.array(range(0,5))
ypoints3 = xpoints * xpoints* xpoints #multiply each entry by itself cubed

plt.plot(xpoints, ypoints, color= 'r',label = "x ")
plt.plot(xpoints, ypoints2, color= 'b',label = "x squared")
plt.plot(xpoints, ypoints3, color= 'g',label = "x cubed")

plt.title("plotask")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.show()
