# 10RandinQueue
# Author: PaulMcGrath
# Task: Create a program that puts 10 random numbers into a queue(list), 
# the program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

import random

queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range (0, numberOfNumbers):
    # i.e. for each n in n= 0 to n = numberOfNumbers (here 10)
    queue.append (random.randint(0,rangeTo))
    # i.e. append to list queue random integers from within 0 and 100
print ("queue is {} " .format (queue))
# the  above prints queue = is {a, b, c,d ] randon numbers
while len(queue) != 0:

    extractedNumber = queue.pop (0)
    # variable extractedNumber = the number that is extracted from the current list
    print ("extracted number is {}  and the remaining queue is {} " .format (extractedNumber , queue))

print ("The queue is now empty")