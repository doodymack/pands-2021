#python collatz.py
# Author: PaulMcGrath
# This program asks the user to input any positive integer
# then At each step calculate the next value by taking the current value
# if it is even, divide it by two, but
# if it is odd, multiply it by three and add one

number = int(input("Please enter a positive integer: "))

numbers = range(1, 10)

sequence_of_numbers = []
for number in numbers:
   if number % 5 in (1, 2):
      sequence_of_numbers.append(number)

print(sequence_of_numbers)

  
