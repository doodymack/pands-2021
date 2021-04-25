# analysis.py
# Author: paul mcgrath

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("iris.csv" ,header=0)

#below plots a scaller plot of the compelete attributes
#further explore ways to have two species attributes on one scatter as per link below
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = data['SepalLengthCm'], y = data['SepalWidthCm'])

#ax[0].scatter(x = data['SepalLengthCm'], y = data['SepalWidthCm'])
#ax[0].set_xlabel('SepalLengthCm')
#ax[0].set_ylabel('SepalWidthCm')
#ax[1].scatter(x = data["PetalLengthCm"], y = data["PetalWidthCm"])
#ax[1].set_xlabel("PetalLengthCm")
#ax[1].set_ylabel("PetalWidthCm")


plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")

plt.show()

#https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
#https://stackoverflow.com/questions/43159754/datasets-load-iris-in-python
#from sklearn.datasets import load_iris
#iris = load_iris()
#features = iris.data.T
#plt.scatter(features[0], features[1], alpha=0.2,
            #s=100*features[3], c=iris.target, cmap='viridis')
#plt.xlabel(iris.feature_names[0])
#plt.ylabel(iris.feature_names[1]);
'''
species_list = list(data["Species"].unique())
print("\nTypes of species: \n{}\n". format(species_list))
print("Dataset length: \t{}\n" . format (len(data)))

print("Sepal length range: \t[{}, {}]" .format (min(data["SepalLengthCm"]) , max(data["SepalLengthCm"])))
print("Sepal width range:  \t[{}, {}]" .format (min(data["SepalWidthCm"]), max(data["SepalWidthCm"])))
print("Petal length range: \t[{}, {}]" .format (min(data["PetalLengthCm"]), max(data["PetalLengthCm"])))
print("Petal width range:  \t[{}, {}]\n" .format (min(data["PetalWidthCm"]), max(data["PetalWidthCm"])))

print("Sepal length mean:\t {:0.3f}" .format ( np.mean(data["SepalLengthCm"])))
print("Sepal width mean: \t {:0.3f}"  .format( np.mean(data["SepalWidthCm"])))
print("Petal length mean:\t {:0.3f}"  .format ( np.mean(data["PetalLengthCm"])))
print("Petal width mean: \t {:0.3f}\n" .format ( np.mean(data["PetalWidthCm"])))

print("Sepal length variance:\t {:0.3f}" .format ( np.var(data["SepalLengthCm"])))
print("Sepal width variance: \t {:0.3f}"  .format( np.var(data["SepalWidthCm"])))
print("Petal length variance:\t {:0.3f}"  .format ( np.var(data["PetalLengthCm"])))
print("Petal width variance: \t {:0.3f}\n"  . format ( np.var(data["PetalWidthCm"])))

print("Sepal length StDev:\t {:0.3f}" .format (np.std(data["SepalLengthCm"])))
print("Sepal width StDev: \t {:0.3f}" .format  (np.std(data["SepalWidthCm"])))
print("Petal length StDev:\t {:0.3f}" .format  (np.std(data["PetalLengthCm"])))
print("Petal width StDev: \t {:0.3f}\n" . format (np.std(data["PetalWidthCm"])))

print("Correlation Matrix:\n --------------------")
corrMatrix = data.corr()
print (corrMatrix)


plt.scatter(x, y, marker='o');

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




plt.hist(DataIS['SepalLengthCm'])
plt.show()

#could this be done with a for loop i.e. for x = {}  with dict item being the column headings
#plt.hist(DataIS[" ", str x)  plt.hist(DataIS[" ".format x)
#but how to label axes too?
#further investigate- look at earlier lessons

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

plt.hist(DataIS_SW)
plt.title ("Iris-Setosa SepalWidthCm")
plt.xlabel("Sepal Width in cm")
plt.ylabel ("Count")

#if you want to save plot as standard i.e. "png" then leave file ending blank which defaults to ".png"
# if you want to sane plot as pdf save as .pdf  or .svg
# plt.savefig('xxxxxx.png', dpi=300)  dpi of 300 increases resolution, add Transparent=True to make plot trsansparent (not recommended)
# facecolor= "blue" gives a blue margin
#The export as vector-based SVG or PDF files is generally preferred over bitmap-based PNG or JPG files
# as they are richer formats, usually providing higher quality plots along with smaller file sizes
plt.savefig("Iris_Setosa_SepalWidth")
plt.show()'''
print ("Hello")
