#weeklytask07
# How_Many_E.py
#Author: Paul Mc Grath
# returns the count of # of letter e in the file in the prompt line 
# e.g. 'python How_Many_E.py  proclamation.txt'
# 
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/
#https://pythonexamples.org/python-count-number-of-characters-in-text-file/

#open file in read mode
##file = open("C:\data.txt", "r")
#read the content of file
##data = file.read()
#get the length of the data
##number_of_characters = len(data)
##print('Number of characters in text file :', number_of_characters)

import sys


file_name = sys.argv[1]
f = open(file_name)
data = f.read()


l="e"
k = 0

for line in data:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)

f.close()
