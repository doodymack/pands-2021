# analysis.py
# Author: paul mcgrath

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("iris.csv")

#to divide data set into three parts:  

iris_setosa=df.loc[df["Species"]=="Iris-setosa"]
iris_virginica=df.loc[df["Species"]=="Iris-virginica"]
iris_versicolor=df.loc[df["Species"]=="Iris-versicolor"]

print(df.head(iris_setosa))
'''
#the below doesn't work likely as seaborn function is not downloaded.
# Further work to use matplotlib and pandas functionality
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"petal_length").add_legend()
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"petal_width").add_legend()
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"sepal_length").add_legend()
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"sepal_width").add_legend()
#plt.show()




#You would give the path, filename etc inside the parenthesis
# Inside the parenthesis you can also pass different arguments that relate to how to open the file.


#In order to convert a certain Python object (dictionary, lists etc) the basic command is:
#pd.DataFrame()

print("First five rows")
print(df.head())
print("*********")
print("columns",df.columns)
print("*********")
print("shape:",df.shape)
print("*********")
print("Size:",df.size)
print("*********")
#print("no of samples available for each type") print(df["type"].value_counts())
print("*********")
print(df.describe())


#df.head(5)
df.info()
df.mean()#Returns the mean of all columns
df.corr()#Returns the correlation between columns in a data frame
df.count()#Returns the number of non-null values in each data frame column
df.max()#Returns the highest value in each column
df.min()#Returns the lowest value in each column
df.median()#Returns the median of each column
df.std()#Returns the standard deviation of each column

# copied from AnalyzingIrisDatasetIdeas.py
# the below works to split data by species and sub split by sttribute
#should allow histograms be created for each attribute
# will need to fins out how to export to png


 print data based on final column variable i.e. string (species)
DataIS = (data.loc[data["Species"]=="Iris-setosa"])
DataIVE = (data.loc[data["Species"]=="Iris-versicolor"])
DataIVI = (data.loc[data["Species"]=="Iris-virginica"])
#print(DataIS.head(5))
#print(DataIVE.head(5))
#print(DataIVI.head(5))

# create a sub data-set based on column i.e. "SepalWidth"
DataIS_SL= DataIS["SepalLengthCm"]
DataIS_SW= DataIS["SepalWidthCm"]
DataIS_PL= DataIS["PetalLengthCm"]
DataIS_PW= DataIS["PetalWidthCm"]
print(DataIS_SL.head(15))
print(DataIS_SW.head(15))
print(DataIS_PL.head(15))
print(DataIS_PW.head(15))

DataIVE_SL= DataIVE["SepalLengthCm"]
DataIVE_SW= DataIVE["SepalWidthCm"]
DataIVE_PL= DataIVE["PetalLengthCm"]
DataIVE_PW= DataIVE["PetalWidthCm"]
print(DataIVE_SL.head(15))
print(DataIVE_SW.head(15))
print(DataIVE_PL.head(15))
print(DataIVE_PW.head(15))

DataIVI_SL= DataIVI["SepalLengthCm"]
DataIVI_SW= DataIVI["SepalWidthCm"]
DataIVI_PL= DataIVI["PetalLengthCm"]
DataIVI_PW= DataIVI["PetalWidthCm"]
print(DataIVI_SL.head(15))
print(DataIVI_SW.head(15))
print(DataIVI_PL.head(15))
print(DataIVI_PW.head(15))

plt.hist(DataIS_SW)
plt.title ("Iris-Setosa SepalWidthCm")
plt.xlabel("Sepal Width in cm")
plt.ylabel ("Count")

plt.show()
'''
print ("Hello")
