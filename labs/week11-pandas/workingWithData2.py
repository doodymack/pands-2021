# import pandas module and use it to create a dataset from a Dict
# Author: Paul Mc Grath
# pd.Series vs pd.Dataset

#import pandas module as pd
import pandas as pd

#create a dataset as dict of lists  
mydataset = {
    'cars' : ["Audi", "Volkswagen", "Mercedes"],
    'passings': [2,4,6]
}

# create a dataset using pandas (pd) module
myvar = pd.DataFrame(mydataset)
#print the full DataFrame
print(myvar)
#print the Dataset from 1st row
print(myvar.loc[0])
#print the Dataset from 2nd row
print(myvar.loc[1])


# add indeces (column 1).  reminder square brackets
myvar = pd.DataFrame(mydataset, ["car 1: ","car 2: ", "car 3:"])
#print the full DataFrame
print(myvar)

#refer to the named index:
print(myvar.loc["car 2: "])

'''
# dataseries (one column) can be created from a list of varied list items
# casn specify which to print 
a = ["one", 7, True]

myvar2 = pd.Series(a, index = ["x", "y", "z"])

print(myvar2["z"])

# create a dataseries from dict- lists calories per day starting with Day 1
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar3 = pd.Series(calories)

print(myvar3)

calories = {"day1": 420, "day2": 380, "day3": 390}
# can select a specific day and print that
myvar4 = pd.Series(calories, index = ["day1", "day2"])

print(myvar4)

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames

'''