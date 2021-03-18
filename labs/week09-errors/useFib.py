#useFib.py
#Author: AndrewBeatty
# program called useFib.py that uses this module (module.py) to prompt a user for a
# number and will return the list of the Fibonacci sequence

import myFunctions #imports my.Functions
howMany = int(input('how many:'))
print(myFunctions.fibonacci(howMany))