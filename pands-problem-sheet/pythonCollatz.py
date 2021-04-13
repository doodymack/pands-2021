#python collatz.py
# Author: PaulMcGrath
# This program asks the user to input any positive integer
# then At each step calculate the next value by taking the current value
# if it is even, divide it by two, but
# if it is odd, multiply it by three and add one
#stops the sequence if number = 1

# https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/
# I tried various versions from stackoverflow with if else loops- none worked

def collatz(n):
    while n > 1:
        print(n, end='  ')
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    print(1, end=' : The End! ')
 
 
n = int(input('Enter n: '))
print('Collatzsequence: ', end='')
collatz(n)
            




'''
if (number % 2 == 0):
    number = (number/2)
else:
    number = ((number*3)+1)

while number !=1:
    print (int(number))
number +=1'''

  
