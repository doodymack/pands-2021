#scatterPlot.py
#Author: Andrew Beatty
# create a scatter plot

import numpy as np
import matplotlib.pyplot as plt

L =20
H = 70
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100
# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(L,H,numberOfEntries) # I don’tlike this, I prefer having absolute values set at the top

plt.scatter(ages, salaries ) # this will be random
#plt.show()

# add x squared
xpoints = np.array(range(L, H))
ypoints = xpoints * xpoints # multiply each entry by itself
plt.plot(xpoints, ypoints, color= 'y',label = "x squared")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.savefig('prettier-plot.png')

#plt.show() # see how the axis have changed