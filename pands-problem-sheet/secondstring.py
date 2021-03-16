# secondstring.py
# author: Paul Mc Grath
# this program reads a string and prints every
# 2nd letter in reverse order

inputString = input (" Enter a sentence: ")
reverseString = inputString [::-1]
reverseString2 = inputString [::-2]
print (" The reverse of your sentence is: \t{}" .format (reverseString))
print (" The sentence with every 2nd letter missing is: \t{}" .format (reverseString2))