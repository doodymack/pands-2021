# salaries.py
# author: Andrew Beatty
#program that makes a list that has x random numbers in a given range

import numpy as np
# it is a good idea to have your absolute values set into variables at the
#beginning of your program
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

# raw prog
min= 20000
max = 80000
num = 10
output = np.random.randint(min, max,num)
print (output)

# raw prog
output = np.random.randint(2,100,5) #outputs 5 random integers between 2 and 100
print (output)