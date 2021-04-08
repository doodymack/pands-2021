# analysisworkings.py
# Author: paul mcgrath
# workings using analysing irisdataset.csv
import pandas as pd 

data = pd.read_csv("iris.csv")
'''#print the 1st 5 rows (if () is empty, or x rows if (x)
print (data.head())
# returns a stats summary table
print (data.describe())
# returns a summary of the dataframe
#can see how many non Nulls there are
print (data.info())

#if you want to get a random sample of rows
print (data.sample(10))

#if you want to print the column titles only
print (data.columns)

#if you want to simply know a. how many rows . how many columns
print (data.shape)

#if you want to print the whole dataset
print(data)

#slicing
#print data from rows 10 to 20
slice = (data[10:21])
print (slice)

extractdata1= data[["Id","SepalLengthCm"]]
print(extractdata1.head(15))
'''
# return the data from a specific row
# loc= index name of the row
# iloc = index integer of the row

#print (data.iloc [5])
print(data.loc[data["Species"]=="Iris-setosa"])
'''
# Create a Histogram for Sepal Length
plt.figure(figsize = (10, 7))
x = data["SepalLengthCm"]

plt.hist(x, bins = 20, color = "blue")
plt.title ("Sepal Length in cm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")'''