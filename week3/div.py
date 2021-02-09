# div.py
# author: paulmcgrath
# # program that reads two numbers and divides the first
# one by the second one. Also gives the integer one and the remainder
x = int(input ("Enter the first number :"))
y = int(input ("Enter the number you want to divide by :"))
answer = int (x/y) #gives the int division
remainder = x%y # gives the remainder

print ("{} divided by {} is {} with remainder {} ".format(x,y,answer,remainder))