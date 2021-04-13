# secondstring.py
# author: Paul Mc Grath
# this program reads a string and prints every
# 2nd letter in reverse order

def reverser(x):
  return x[::-1]

def everysecond(x):
    return x[::-2]


inputString = input (" Enter a sentence: ")
reverseString = reverser(inputString)

reverseString2 = everysecond(inputString)

print ()
print (" The reverse of your sentence is: \t{}" .format (reverseString))
print (" \nThe sentence with every 2nd letter missing is: \t{}" .format (reverseString2))
print ()

# The format for slice notation is [start:stop:step].
#  So, [::2] is telling Python to step through the string by 2's (which will return every other character).
# source: https://www.w3schools.com/python/python_howto_reverse_string.asp
# source: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220
