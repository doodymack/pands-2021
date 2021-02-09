# absolute.py
# gives the absolute value for an inputted value
# author: paul mc grath
# 'number' ambiguous- output implies we are dealing with a number 
# therefore casting the input to a float

number = float(input(" Enter a number "))
absoluteNumber = abs(number)
print ('The absolute value of {} is {}' .format (number, absoluteNumber))