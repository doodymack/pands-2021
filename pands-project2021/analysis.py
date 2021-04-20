# analysisIdeasUsingPanda.py
# Author: paul mcgrath

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673
# When you want to use Pandas for data analysis, you’ll usually use it in one of three different ways:
#Convert a Python’s list, dictionary or Numpy array to a Pandas data frame
#Open a local file using Pandas, usually a CSV file, but could also be a delimited text file (like TSV), Excel, etc
#Open a remote file or database like a CSV or a JSONon a website through a URL or read from a SQL table/database
#There are different commands to each of these options, but when you open a file, they would look like this:
# 
# pd.read_filetype()
#df = pd.read_csv('irisdata.csv', index_col=0)
col=['sepal_length','sepal_width','petal_length','petal_width','type']

df=pd.read_csv("irisdata.csv",names=col)

#to divide data set into three parts:

iris_setosa=df.loc[df["type"]=="Iris-setosa"]
iris_virginica=df.loc[df["type"]=="Iris-virginica"]
iris_versicolor=df.loc[df["type"]=="Iris-versicolor"]


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
'''
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
df.info()'''
df.mean()#Returns the mean of all columns
df.corr()#Returns the correlation between columns in a data frame
df.count()#Returns the number of non-null values in each data frame column
df.max()#Returns the highest value in each column
df.min()#Returns the lowest value in each column
df.median()#Returns the median of each column
df.std()#Returns the standard deviation of each column
print ("Hello")
