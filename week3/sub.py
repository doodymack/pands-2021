# sub.py
#author:PaulMcGrath
# program to ask for user to input two numbers
# program subtracts seconf number from first and prints the answer
# input reads the input as a str which cannot be used in algebra
#thus need to convet str to int

x = int(input (' enter the first number: '))
y = int(input (' enter the second number: '))
answer = x-y
print (" {} minus {} equals {} ".format (x ,y , answer))