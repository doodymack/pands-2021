# Messing with Files2.py
#Author: Paul Mc Grath
# reads in a number from chosen file & overwrites that file with that number

#filename = "count.txt"
#def writeNumber(number):
   # with open(filename, "wt") as f:
 # write takes a string so we need to convert
       # f.write(str(number))
# test it
#writeNumber(300)

filename = "count2.txt"
def writeNumber(number):
    with open(filename, "w") as f:
        f.write(str(number))
writeNumber(100)