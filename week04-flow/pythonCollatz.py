#python collatz.py
# Author: PaulMcGrath
# This program asks the user to input any positive integer
# then At each step calculate the next value by taking the current value
# if it is even, divide it by two, but
# if it is odd, multiply it by three and add one

number = int(input("Please enter a positive integer: "))

if (number % 2 == 0):
    number = (number/2)
else:
    number = ((number*3)+1)

while number !=1:
    print (int(number))


  
