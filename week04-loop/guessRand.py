# guessRand.py
# Author: Paul McGrath
# this program creates a random number in the range
# it gives a hint -number is higher or lower

import random  

numberToGuess = random.randint (0,100)  #this is the range 1-99. 
# found in tutorialpoint.com.  other optiomns on stackoverflow
#but this was the most elegant

guess = int(input ("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
         print (" number is higher")
    else:
        print (" number is lower")
    guess = int(input ("Please guess again: "))

print ("Well done!  Yes the Number is {}!"  .format(numberToGuess))

