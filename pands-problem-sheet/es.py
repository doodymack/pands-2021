#weeklytask07
# howManyE.py
#Author: Paul Mc Grath
# asks the user to input a file name
# adapted from how many letter source:
# https://www.sanfoundry.com/python-program-read-file-counts-number/
#Program Explanation
#1. User must enter a file name and the letter to be searched.
#2. The file is opened using the open() function in the read mode.
#3. A for loop is used to read through each line in the file.
#4. Each line is split into a list of words using split().
#5. A for loop is used to traverse through the words list and another for loop is
#  used to traverse through the letters in the word.
#6. If the letter provided by the user and the letter encountered over iteration are
#  equal, the letter count is incremented.
#7. The final count of occurrences of the letter is printed.

fname = input("Enter file name: ")
l="e"
k = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)