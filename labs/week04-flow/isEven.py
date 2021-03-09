# isEven.py
# Author:PaulMcGrath
#  asks for user to enter a number
# program will tell user if the number is even
# note comma in front of format works same as full stop
# note '+str(number))' works as well
# note if use "+" in front of format it outputs '{} is an even number66'

number = int(input("enter an integer: "))

if (number % 2 == 0):
    print ("{} is an even number" +str(number))
else:
    print ("{} is an odd number" .format(number))
