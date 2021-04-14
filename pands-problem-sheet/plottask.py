#plottask.py
#Author: PaulMcGrath
# displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# in a nice looking plot
#https://www.w3schools.com/python/matplotlib_plotting.asp
# https://realpython.com/python-matplotlib-guide/
#https://matplotlib.org/stable/
# https://github.com/matplotlib/cheatsheets#cheatsheets
#https://github.com/pandas-dev/pandas




import matplotlib.pyplot as plt #imports matplotlib module renameit as "plt"

import numpy as np #imports numpy module as "np"


xpoints = np.array(range(0,5))
ypoints = xpoints  #multiply each entry by itself

#xpoints = np.array(range(0,5))
ypoints2 = xpoints * xpoints #multiply each entry by itself squared

#xpoints = np.array(range(0,5))
ypoints3 = xpoints * xpoints* xpoints #multiply each entry by itself cubed

# plt.plot(xpoints, ypoints, 'o', color= 'r',label = "x ")  'o' will plot data points only 
# linestyle = 'ls', ':' = dotted '--' = dashed;  marker= see W3 schools as above link
# linewidth = 'lw'

#you can plot as many lines as you like by simply adding more plt.plot() functions:
plt.plot(xpoints, ypoints, marker = '^', color= 'r',label = "x ")
plt.plot(xpoints, ypoints2, marker = 'v', color= 'b', ls = '--', label = "x squared")
plt.plot(xpoints, ypoints3, marker = 'D', color= 'g', ls = ':',label = "x cubed")



plt.title("plottask-displays a plot of the functions\n f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]")
plt.xlabel("X value")
plt.ylabel("Y value")
plt.legend()

plt.show()
