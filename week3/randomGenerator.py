# randomGenerator/py
# author: PaulMcGrath
# prints out a random number

import random
A = int(input ("give me a number: "))
B = int(input ("give me a second number: "))
Number = random.randint (A,B)
print ("Here is a random number between {} and {} = {}" .format (A,B,Number))