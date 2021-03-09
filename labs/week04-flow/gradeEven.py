#grade.py
#Author: Paul McGrath
# This prograsn reads in a students percentage
#  and prints out the corresponding grade
# i.e. under 40% Fail, 40-49% Pass, 50-59% Merit2, 60-69%Merit1, Over 70% Distinction
# reminder: float is a number thats not an integer
# dont use 'if' condition 'is'  i.e. leave out 'is'

percentage = float(input ("Input the percentage: "))

integer = int(percentage) # converts float to an integer- but doesnt round up 69.5 =merit
if integer < 0 or percentage > 100:
    print ("please input as number between 0 and 100") #this stops the program
elif  integer < 40: # can add comments in same line once
    # colon can continue comments even in middle of loop- handy!
    print ("Fail")
elif integer < 50: 
    print ("Pass")
elif integer < 60: 
    print ("Merit2")
elif integer < 70: 
    print ("Merit2")
else: print ("Distinction")