# analysis.py
# Author: paul mcgrath

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt



#Open a local file using Pandas, usually a CSV file,
#You would give the path, filename etc inside the parenthesis
# Inside the parenthesis you can also pass different arguments that relate to how to open the file.
pd.read_filetype()
df = pd.read_csv('data.csv', index_col=0)

#In order to convert a certain Python object (dictionary, lists etc) the basic command is:
pd.DataFrame()
#Viewing and Inspecting Data
#Now that you’ve loaded your data, it’s time to take a look. How does the data frame look? 
# Running the name of the data frame would give you the entire table, but you can also 
# get the first n rows with df.head(n) or the last n rows with df.tail(n).
#  df.shape would give you the number of rows and columns. df.info() would give you the index,
#  datatype and memory information. 
# The command s.value_counts(dropna=False) would allow you to view unique values and counts for a series 
# (like a column or a few columns). A very useful command is df.describe() 
# which inputs summary statistics for numerical columns. 
# It is also possible to get statistics on the entire data frame or a series (a column etc):
df.mean()#Returns the mean of all columns
df.corr()#Returns the correlation between columns in a data frame
df.count()#Returns the number of non-null values in each data frame column
df.max()#Returns the highest value in each column
df.min()#Returns the lowest value in each column
df.median()#Returns the median of each column
df.std()#Returns the standard deviation of each column

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
