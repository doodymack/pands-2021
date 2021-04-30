# old code.py
# Author: Paul McGrath
# deposit of no longer required code for analysing Fisher Dataset


# below used to work with print - find out why doesnt work now
#file.write("Sepal length range: \t[{}, {}]\n" .format (min(data["SepalLengthCm"]) , max(data["SepalLengthCm"])))
#file.write("Iris Setosa Sepal width range:  \t[{}, {}]\n" .format (min(data["SepalWidthCm"]) max(data["SepalWidthCm"])))
#file.write("Iris Setosa Petal length range: \t[{}, {}]\n" .format (min(data["PetalLengthCm"]), max(data["PetalLengthCm"])))
#file.write("Iris Setosa Petal width range:  \t[{}, {}]\n" .format (min(data["PetalWidthCm"]), max(data["PetalWidthCm"])))

#file.write("Iris Setosa Sepal length mean:\t {:0.3f}\n" .format ( np.mean(data["SepalLengthCm"])))
#file.write("Iris Setosa Sepal width mean: \t {:0.3f}\n"  .format( np.mean(data["SepalWidthCm"])))
#file.write("Iris Setosa Petal length mean:\t {:0.3f}\n"  .format ( np.mean(data["PetalLengthCm"])))
#file.write("Iris Setosa Petal width mean: \t {:0.3f}\n" .format ( np.mean(data["PetalWidthCm"])))

#file.write("Iris Setosa Sepal length variance:\t {:0.3f}\n" .format ( np.var(data["SepalLengthCm"])))
#file.write("Iris Setosa Sepal width variance: \t {:0.3f}\n"  .format( np.var(data["SepalWidthCm"])))
#file.write("Iris Setosa Petal length variance:\t {:0.3f}\n"  .format ( np.var(data["PetalLengthCm"])))
#file.write("Iris Setosa Petal width variance: \t {:0.3f}\n"  . format ( np.var(data["PetalWidthCm"])))

#file.write("Iris Setosa Sepal length StDev:\t {:0.3f}\n" .format (np.std(data["SepalLengthCm"])))
#file.write("Iris Setosa Sepal width StDev: \t {:0.3f}\n" .format  (np.std(data["SepalWidthCm"])))
#file.write("Iris Setosa Petal length StDev:\t {:0.3f}\n" .format  (np.std(data["PetalLengthCm"])))
#file.write("Iris Setosa Petal width StDev: \t {:0.3f}\n" . format (np.std(data["PetalWidthCm"])))



'''
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


#the below doesn't work likely as seaborn function is not downloaded.
# Further work to use matplotlib and pandas functionality
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"petal_length").add_legend()
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"petal_width").add_legend()
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"sepal_length").add_legend()
#sns.FacetGrid(df,hue="type",size=3).map(sns.distplot,"sepal_width").add_legend()
#plt.show()

# have a look at this to get visual correlations- uses seaborn.  Try to use use matplotlib/pandas first
#https://datatofish.com/correlation-matrix-pandas/

print("Data describe\n---")
#print(data[data.columns[2:]].describe())

print ("The overall mean is")
print (data.mean(axis=0))

print ("The # of non-null values is")
print (data.count(axis=0))

print ("The overall median is")
print (data.median(axis=0))

#print ("The overall max is")
#print (data.max(axis=0))

#print ("The overall min is")
#print (data.min(axis=0))


#to divide data set into three parts:  

iris_setosa=df.loc[df["Species"]=="Iris-setosa"]
iris_virginica=df.loc[df["Species"]=="Iris-virginica"]
iris_versicolor=df.loc[df["Species"]=="Iris-versicolor"]

(df.head(iris_setosa))


#You would give the path, filename etc inside the parenthesis
# Inside the parenthesis you can also pass different arguments that relate to how to open the file.

rint("First five rows")
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


#In order to convert a certain Python object (dictionary, lists etc) the basic command is:
pd.DataFrame(data)

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


data.head(5)
#data.info()
print(data.mean())#Returns the mean of all columns
data.corr()#Returns the correlation between columns in a data frame
data.count()#Returns the number of non-null values in each data frame column
data.max()#Returns the highest value in each column
data.min()#Returns the lowest value in each column
data.median()#Returns the median of each column
data.std()#Returns the standard deviation of each column

# copied from AnalyzingIrisDatasetIdeas.py
# the below works to split data by species and sub split by attribute
#should allow histograms be created for each attribute


#print data based on final column variable i.e. string (species)
DataIS = (data.loc[data["Species"]=="Iris-setosa"])
DataIVE = (data.loc[data["Species"]=="Iris-versicolor"])
DataIVI = (data.loc[data["Species"]=="Iris-virginica"])

#below dosent work
#data.mean(DataIS['SepalLengthCm'])
np.min(DataIS['SepalLengthCm'])


#print(DataIS.head(5))
#print(DataIVE.head(5))
#print(DataIVI.head(5))

#unsure if need to split data up further for histograms i.e .above works to extract the individual columns
#into as histogram. 
#May be needed for correlations and summary stats- further research required.

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

#print("Hello stackoverflow!", file=open("test2.txt", "a"))
#print("I have a question.", file=open("test2.txt", "a"))

#with open("test.txt", "a") as f:
    #print("Hello stackoverflow!", file=f)

#import sys
#sys.stdout = open('test.txt','wt')
#print ("Hello stackoverflow!")
#print ("I have a question.")

#def append():
    #text_file = open("Test2.txt", "a")
    #text_file.write("\n",f)

#species_list = list(data["Species"].unique())

#file.write("\nTypes of species: \n{}\n". format(species_list))
#file.write("Dataset length: \t{}\n" . format (len(data)))
#file.close()

#Returns the mean of all columns
#df.corr()#Returns the correlation between columns in a data frame
#df.count()#Returns the number of non-null values in each data frame column
#df.max()#Returns the highest value in each column
#df.min()#Returns the lowest value in each column
#df.median()#Returns the median of each column
#df.std()

plt.hist(DataIS['SepalLengthCm'])
#plt.legend(['Red'])
#plt.show()

#could this be done with a for loop i.e. for x = {}  with dict item being the column headings
#plt.hist(DataIS[" ", str x)  plt.hist(DataIS[" ".format x)
#but how to label axes too?
#further investigate- look at earlier lessons

# to save histograms as png:
#if you want to save plot as standard i.e. "png" then leave file ending blank which defaults to ".png"
# if you want to sane plot as pdf save as .pdf  or .svg
# plt.savefig('xxxxxx.png', dpi=300)  dpi of 300 increases resolution, add Transparent=True to make plot trsansparent (not recommended)
# facecolor= "blue" gives a blue margin
#The export as vector-based SVG or PDF files is generally preferred over bitmap-based PNG or JPG files
# as they are richer formats, usually providing higher quality plots along with smaller file sizes
#plt.savefig("Iris_Setosa_SepalWidth")
#plt.show()

 saving multiple files
 for spot, group in df.set_index('spot', append=True).groupby(level='spot'):
    group.plot(kind = 'bar, figsize = (12,6))
    plt.savefig('{}.png'.format(spot))



#data.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")

## https://www.kaggle.com/zachgold/python-iris-data-visualizations
#  One piece of information missing in the plots above is what species each plant is
# We'll use seaborn's FacetGrid to color the scatterplot by species. That's what 
# hue="Species" is for in the 1st line below!
# I've also added a parameter to the FacetGrid function for color palette. Here it's 
# set to husl.




#below plots a scatter plot of the compelete attributes
#further explore ways to have two species attributes on one scatter as per link below

#fig, ax = plt.subplots(figsize=(10, 6))
#ax.scatter(x = data['SepalLengthCm'], y = data['SepalWidthCm'])
#ax[1].scatter(x = data["PetalLengthCm"], y = data["PetalWidthCm"])

#ax[0].scatter(x = data['SepalLengthCm'], y = data['SepalWidthCm'])
#ax[0].set_xlabel('SepalLengthCm')
#ax[0].set_ylabel('SepalWidthCm')
#ax[1].scatter(x = data["PetalLengthCm"], y = data["PetalWidthCm"])
#ax[1].set_xlabel("PetalLengthCm")
#ax[1].set_ylabel("PetalWidthCm")

# print("Correlation Matrix:\n --------------------")
# corrMatrix = data.corr()
# print (corrMatrix)


# plt.scatter(x, y, marker='o');

#plt.xlabel("SepalLengthCm")
#plt.ylabel("SepalWidthCm")

plt.show()


# https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
#https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python

# this didnt work- may be worth looking further if have time to see if anything uesful

#from sklearn.datasets import load_iris
#iris = load_iris()
#features = iris.data.T
#plt.scatter(features[0], features[1], alpha=0.2,
            #s=100*features[3], c=iris.target, cmap='viridis')
#plt.xlabel(iris.feature_names[0])
#plt.ylabel(iris.feature_names[1]);

print ("Hello")

#Selection of Data
#One of the things that is so much easier in Pandas 
# is selecting the data you want in comparison to selecting a value from a list or a dictionary.
#  You can select a column
(df[col])
#and return column with label col as Series or a few columns
(df[[col1, col2]])
#and returns columns as a new DataFrame.
#You can select by position
(s.iloc[0]) 
#or by index 
(s.loc['index_one'])
 #In order to select the first row you can use 
 df.iloc[0,:]
 #and in order to select the first element of the first column you would run 
 df.iloc[0,0]
 #These can also be used in different combinations, so I hope it gives you an 
 # idea of the different selection and indexing you can perform in Pandas.

 #Filter, Sort and Groupby
#You can use different conditions to filter columns. For example
df[df[year] > 1984]
#would give you only the column year is greater than 1984. 
# You can use & (and) or | (or) to add different conditions to your filtering.
#  This is also called boolean filtering.

# It is possible to sort values in a certain column in an ascending order using
df.sort_values(col1)
#and also in a descending order using
df.sort_values(col2,ascending=False)
#Furthermore, it’s possible to sort values by col1 in ascending order then col2 in descending order by using
df.sort_values([col1,col2],ascending=[True,False])

#The last command in this section is groupby.
# It involves splitting the data into groups based on some criteria,
# applying a function to each group independently and combining the results into a data structure.
df.groupby(col) #returns a groupby object for values from one column while
df.groupby([col1,col2])
#returns a groupby object for values from multiple columns.

#Data Cleaning
#Data cleaning is a very important step in data analysis.
# For example, we always check for missing values in the data by running#
pd.isnull()
#which checks for null Values, and returns a boolean array#
# (an array of true for missing values and false for non-missing values).
#  In order to get a sum of null/missing values, run#
pd.isnull().sum(). pd.notnull() #is the opposite of pd.isnull()
#After you get a list of missing values you can get rid of them, or drop them by using
df.dropna()
# to drop the rows or#
df.dropna(axis=1)
#to drop the columns. A different approach would be to fill the missing values with other values by using#
df.fillna(x)
#which fills the missing values with x (you can put there whatever you want) or 
s.fillna(s.mean())
# to replace all null values with the mean (mean can be replaced with almost any function from the statistics section).
#It is sometimes necessary to replace values with different values.
#  For example
s.replace(1,'one')
# would replace all values equal to 1 with 'one'. It’s possible to do it for multiple values:
s.replace([1,3],['one','three'])
# would replace all 1 with 'one' and 3 with 'three'.
#  You can also rename specific columns by running:
df.rename(columns={'old_name': 'new_ name'})
#or use
df.set_index('column_one')# to change the index of the data frame.

#Join/Combine
#The last set of basic Pandas commands are for joining or combining data frames or rows/columns.
#  The three commands are:
df1.append(df2) # add the rows in df1 to the end of df2 (columns should be identical)
df.concat([df1, df2],axis=1) # add the columns in df1 to the end of df2 (rows should be identical)
df1.join(df2,on=col1,how='inner') # SQL-style join the columns in df1
#with the columns on df2 where the rows for colhave identical values.
#  how can be equal to one of: 'left', 'right', 'outer', 'inner'

#from weekly tasks the following might be useful for plotting
# you can plot as many lines as you like by simply adding more plt.plot() functions:
#plt.plot(xpoints, ypoints, marker = '^', color= 'r',label = "x ")
#plt.plot(xpoints, ypoints2, marker = 'v', color= 'b', ls = '--', label = "x squared")
#plt.plot(xpoints, ypoints3, marker = 'D', color= 'g', ls = ':',label = "x cubed")

#scatter plots
# https://www.w3schools.com/python/matplotlib_scatter.asp
# plt.scatter(x, y, color = '#88c999')
# plt.show()


# correlations using matplotlib & numpy: 

# x = numpy.std(y)
#print(x)


# LinearRegression:

# from scipy import stats
#Execute a method that returns some important key values of Linear Regression:
#slope, intercept, r, p, std_err = stats.linregress(x, y)

# create a function that uses the slope of the line and intercept to draw a line

#def myfunc(x):
  #return slope * x + intercept

#mymodel = list(map(myfunc, x))

# plot the new line
#plt.scatter(x, y)
#plt.plot(x, mymodel)
#plt.show()
#what is r? can you do r2 also? - more research

#print(r)

## how to get r on the linear regrerssion plot as i.e. legend

#Create Histogram
#https://www.w3schools.com/python/matplotlib_histograms.asp
#https://github.com/matplotlib/matplotlib
# In Matplotlib, we use the hist() function to create histograms.
# The hist() function will use an array of numbers to create a histogram,
# the array is sent into the function as an argument.
# plt.hist(x)
# plt.show() 

#From weekly task 'plottask1- may be of use?
#plt.title("plottask-displays a plot of the functions\n f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]")
#plt.xlabel("X value")
#plt.ylabel("Y value")
#plt.legend()

#plt.show()



#from sklearn.datasets import load_iris
#data = load_iris()

#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html
 
# Pandas is an open source Python package that is most widely used for 
# data science/data analysis and machine learning tasks.
#  It is built on top of another package named Numpy,
#  which provides support for multi-dimensional arrays

import pandas as pd 

#NumPy is an open-source numerical Python library. 
# NumPy contains a multi-dimensional array and matrix data structures.
# It can be utilised to perform a number of mathematical operations on arrays such as
#  trigonometric, statistical, and algebraic routines.
#  Pandas objects rely heavily on NumPy objects

import numpy as np

#Matplotlib is a plotting library for the Python programming language
# and its numerical mathematics extension NumPy
# #matplotlib is required for creating a histogram

import matplotlib.pyplot as plt


data = pd.read_csv("iris.csv")


#print the 1st 5 rows (if () is empty, or x rows if (x)
print (data.head(6))

# returns a stats summary table
#print (data.describe())

# returns a summary of the dataframe
#can see how many non Nulls there are
#print (data.info())

#if you want to get a random sample of rows
#print (data.sample(10))

#if you want to print the column titles only
#print (data.columns)

#if you want to simply know a. how many rows b. how many columns
#print (data.shape)

#if you want to print the whole dataset
#print(data)

#slicing
#print data from rows 10 to 20
#slice = (data[10:21])
#print (slice)

#sort by column i.e. sepal width and print column data
# create a histogram of the combined column data
#extractdata1= data["SepalWidthCm"]
#print(extractdata1.head(15))
#plt.hist(extractdata1)

#plt.show()


# return the data from a specific Row
# loc= index name of the row
# iloc = index integer of the row

#print (data.iloc [5])
#print rows with specified data i.e. number.  Note can't use "4.7" as its not a string but integer
# can also print all of one species if select by species -this time its a string so need "  "
#print(data.loc[data["PetalLengthCm"]==4.8])

# print data based on final column variable i.e. string (species)
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

#DataIVI = (data.loc[data["Species"]=="Iris-virginica"])
#print(DataIVI.head(15))

#DataIVE = (data.loc[data["Species"]=="Iris-versicolor"])
#print(DataIVE.head(15))

# The value_counts() function, counts the number of times a particular instance or data has occurred
#print (data["Species"].value_counts())

# Calculating basic statisitics per column i.e. sum, mean,median, min & max
# data["column_name"].x()  where "x" = sum/mean/median
#sumSepalLength= data["SepalLengthCm"].sum()
#meanSepalLength= data["SepalLengthCm"].mean()
#medianSepalLength= data["SepalLengthCm"].median()
#minSepalLength= data["SepalLengthCm"].min()
#maxSepalLength= data["SepalLengthCm"].max()

# \n = new line if use \t = tab
#print ("Statistics for SepalLengthCm :")
#print("\nSum:",sumSepalLength, "\nMean:",meanSepalLength , "\nMedian:",
#medianSepalLength,"\nMin:",minSepalLength,"\nMax:",maxSepalLength)

#

#data.isnull()
#print (data.isnull)

# keep working on basic stats to get histograms of each attribute per species
# once these can be created research on the correlations.
# only when these are working go back to code and look for potential for improvement

#Create a Histogram for Sepal Length
#https://realpython.com/courses/python-histograms/

#pd.plt.figure(figsize = (10, 7))
#x = np.data["SepalLengthCm"]
#plt.pyplot.hist()
#plt.hist(x, bins = 20, color = "blue")
#plt.title ("Sepal Length in cm")
#plt.xlabel("Sepal Length in cm")
#plt.ylabel ("Count")
#plt.show()

#plt.hist(data [] bins =10)
#data.hist()
#plt.show()

# summary scatter plot matrix- doesn't work
#scatter_matrix(data)

#plt.show()
