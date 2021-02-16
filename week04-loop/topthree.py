#topthree.py
#Author: PaulMcGrath
# generates three randon mumbers 0-100, prints them out, prints the top three
# uses a list to store and manipulate them

import random

HowMany = 20
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range (0,HowMany): #this defines the number of numbers in the list
# highest value not included
    numbers.append(random.randint (rangeFrom,rangeTo)) # what does this do?
print (" {} random numbers\t {}" .format (HowMany,numbers)) # \t puts a tab 

# uses the list from above for a further function
topOnes = numbers.copy () # what is copy function here?
print ("{}\t\t\t" .format (topOnes)) # to confirm that it does copy the list as is
topOnes.sort(reverse=True) #sorts the numbers in reverse order
print ("{} ". format (topOnes)) # to confirm the list is reversed
print ("The top {} are\t\t {} " .format (topHowMany, topOnes[0:topHowMany])) 
# the line of code  lists the top "3" i.e. "TopHowmany" in the list