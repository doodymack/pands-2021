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
'''
#extractdata1= data[["Id","SepalLengthCm"]]
#print(extractdata1.head(15))

#IrisSetosaData= data["Species","Iris-setosa"]
#print(IrisSetosaData.head(15))

# return the data from a specific Row
# loc= index name of the row
# iloc = index integer of the row

#print (data.iloc [5])
#print rows with specified data i.e. number.  Note can't use "4.7" as its not a string but integer
# can also print all of one species if select by species -this time its a string so need "  "
#print(data.loc[data["PetalLengthCm"]==4.8])

# print data based on final column variable i.e. string (species)
'''DataIS = (data.loc[data["Species"]=="Iris-setosa"])
print(DataIS.head(15))

DataIVI = (data.loc[data["Species"]=="Iris-virginica"])
print(DataIVI.head(15))

DataIVE = (data.loc[data["Species"]=="Iris-versicolor"])
print(DataIVE.head(15))
'''
# The value_counts() function, counts the number of times a particular instance or data has occurred
print (data["Species"].value_counts())

# Calculating basic statisitics per column i.e. sum, mean,median, min & max
# data["column_name"].x()  where "x" = sum/mean/median
sumSepalLength= data["SepalLengthCm"].sum()
meanSepalLength= data["SepalLengthCm"].mean()
medianSepalLength= data["SepalLengthCm"].median()
minSepalLength= data["SepalLengthCm"].min()
maxSepalLength= data["SepalLengthCm"].max()

# \n = new line if use \t = tab
print ("Statistics for SepalLengthCm :")
print("\nSum:",sumSepalLength, "\nMean:",meanSepalLength , "\nMedian:",
medianSepalLength,"\nMin:",minSepalLength,"\nMax:",maxSepalLength)

# find out  whats happening here   https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

data.isnull()
print (data.isnull)

# keep working on basic stats to get histograms of each attribute per species
# once these can be created reseatch on the correlations.
# only when these are working go back to code and look for potential for improvement
'''
# Create a Histogram for Sepal Length
plt.figure(figsize = (10, 7))
x = data["SepalLengthCm"]

plt.hist(x, bins = 20, color = "blue")
plt.title ("Sepal Length in cm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")'''