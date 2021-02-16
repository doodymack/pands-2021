#average.py
#Author: Paul McGrath
#  asks user to enter a number = the script then lists the numbers and gives an average

numbers = [] # numbers plural as list

number = int(input("Enter a number (0 to quit):")) # error if put in a float n ot an integer

while number != 0:

    numbers.append(number)  # adds the inputted number to the list 'numbers'
    number = int(input("Enter another number (0 to quit):"))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)

print ("The average is {}" .format(average))