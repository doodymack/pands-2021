#grade.py
#Author: Paul McGrath
# This prograsn reads in a students percentage
#  and prints out the corresponding grade
# i.e. under 40% Fail, 40-49% Pass, 50-59% Merit2, 60-69%Merit1, Over 70% Distinction
# reminder: float is s number thats not an integer
# dont use 'if' condition 'is'  i.e. leave out 'is'

percentage = float(input ("Input the percentage: "))

if percentage < 0 or percentage > 100:
    print ("please input as number between 0 and 100") #this stops the program
elif  percentage < 40: # can add comments in same line once
    # once colon can continue comments
    print ("Fail")
elif percentage < 50: 
    print ("Pass")
elif percentage < 60: 
    print ("Merit2")
elif percentage < 70: 
    print ("Merit2")
else: print ("Distinction")