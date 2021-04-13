#weeklytask07
# howManyE.py
#Author: Paul Mc Grath


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
