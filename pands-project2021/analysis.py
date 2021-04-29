# analysis.py
# Author: paul mcgrath


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("iris.csv" ,header=0)

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



file = open("Test2.txt" ,"w")

#species_list = list(data["Species"].unique())

#file.write("\nTypes of species: \n{}\n". format(species_list))
#file.write("Dataset length: \t{}\n" . format (len(data)))
#file.close()


###
### Number 1:  a summary of each variable outputted to a single text file (append)



species_list = list(data["Species"].unique())

file.write("\nTypes of species: \n{}\n". format(species_list))

file.write("Dataset length: \t{}\n\n" . format (len(data)))

file.write("Sepal length range: \t[{}, {}]\n" .format (min(data["SepalLengthCm"]) , max(data["SepalLengthCm"])))
file.write("Sepal width range:  \t[{}, {}]\n" .format (min(data["SepalWidthCm"]), max(data["SepalWidthCm"])))
file.write("Petal length range: \t[{}, {}]\n" .format (min(data["PetalLengthCm"]), max(data["PetalLengthCm"])))
file.write("Petal width range:  \t[{}, {}]\n" .format (min(data["PetalWidthCm"]), max(data["PetalWidthCm"])))

file.write("Sepal length mean:\t {:0.3f}\n" .format ( np.mean(data["SepalLengthCm"])))
file.write("Sepal width mean: \t {:0.3f}\n"  .format( np.mean(data["SepalWidthCm"])))
file.write("Petal length mean:\t {:0.3f}\n"  .format ( np.mean(data["PetalLengthCm"])))
file.write("Petal width mean: \t {:0.3f}\n" .format ( np.mean(data["PetalWidthCm"])))

file.write("Sepal length variance:\t {:0.3f}\n" .format ( np.var(data["SepalLengthCm"])))
file.write("Sepal width variance: \t {:0.3f}\n"  .format( np.var(data["SepalWidthCm"])))
file.write("Petal length variance:\t {:0.3f}\n"  .format ( np.var(data["PetalLengthCm"])))
file.write("Petal width variance: \t {:0.3f}\n"  . format ( np.var(data["PetalWidthCm"])))

file.write("Sepal length StDev:\t {:0.3f}\n" .format (np.std(data["SepalLengthCm"])))
file.write("Sepal width StDev: \t {:0.3f}\n" .format  (np.std(data["SepalWidthCm"])))
file.write("Petal length StDev:\t {:0.3f}\n" .format  (np.std(data["PetalLengthCm"])))
file.write("Petal width StDev: \t {:0.3f}\n\n" . format (np.std(data["PetalWidthCm"])))


DataIS = (data.loc[data["Species"]=="Iris-setosa"])
DataIVE = (data.loc[data["Species"]=="Iris-versicolor"])
DataIVI = (data.loc[data["Species"]=="Iris-virginica"])

# Dataframe sliced per species

file.write("Iris Setosa Attributes:\n\n")

DataIS_SL= DataIS["SepalLengthCm"]
DataIS_SW= DataIS["SepalWidthCm"]
DataIS_PL= DataIS["PetalLengthCm"]
DataIS_PW= DataIS["PetalWidthCm"]


# Export summary of variables of Iris Setosa (Data split)
file.write("Iris Setosa Sepal Length min:\t{:0.3f}\n" .format (np.min([DataIS_SL])))
file.write("Iris Setosa Sepal Length max:\t{:0.3f}\n" .format (np.max([DataIS_SL])))
file.write("Iris Setosa Sepal length mean:\t {:0.3f}\n" .format (np.mean([DataIS_SL])))
file.write("Iris Setosa Sepal Length var:\t{:0.3f}\n" .format (np.var([DataIS_SL])))
file.write("Iris Setosa Sepal Length StDev:\t{:0.3f}\n\n" .format (np.std([DataIS_SL])))

file.write("Iris Setosa Sepal Width min:\t{:0.3f}\n" .format (np.min([DataIS_SW])))
file.write("Iris Setosa Sepal Width max:\t{:0.3f}\n" .format (np.max([DataIS_SW])))
file.write("Iris Setosa Sepal Width mean:\t {:0.3f}\n" .format (np.mean([DataIS_SW])))
file.write("Iris Setosa Sepal Width var:\t{:0.3f}\n" .format (np.var([DataIS_SW])))
file.write("Iris Setosa Sepal Width StDev:\t{:0.3f}\n\n" .format (np.std([DataIS_SW])))

file.write("Iris Setosa PetalLengthCm min:\t{:0.3f}\n" .format (np.min([DataIS_PL])))
file.write("Iris Setosa PetalLengthCm max:\t{:0.3f}\n" .format (np.max([DataIS_PL])))
file.write("Iris Setosa PetalLengthCm mean:\t {:0.3f}\n" .format (np.mean([DataIS_PL])))
file.write("Iris Setosa PetalLengthCm var:\t{:0.3f}\n" .format (np.var([DataIS_PL])))
file.write("Iris Setosa PetalLengthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIS_PL])))

file.write("Iris Setosa PetalWidthCm min:\t{:0.3f}\n" .format (np.min([DataIS_PW])))
file.write("Iris Setosa PetalWidthCm max:\t{:0.3f}\n" .format (np.max([DataIS_PW])))
file.write("Iris Setosa PetalWidthCm mean:\t {:0.3f}\n" .format (np.mean([DataIS_PW])))
file.write("Iris Setosa PetalWidthCm var:\t{:0.3f}\n" .format (np.var([DataIS_PW])))
file.write("Iris Setosa PetalWidthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIS_PW])))

# Dataframe sliced per species
DataIVE_SL= DataIVE["SepalLengthCm"]
DataIVE_SW= DataIVE["SepalWidthCm"]
DataIVE_PL= DataIVE["PetalLengthCm"]
DataIVE_PW= DataIVE["PetalWidthCm"]


# Export summary of variables of Iris Versicolor (Data split)
file.write("Iris Versicolor Attributes:\n\n")

file.write("Iris Versicolor Sepal Length min:\t{:0.3f}\n" .format (np.min([DataIVE_SL])))
file.write("Iris Versicolor Sepal Length max:\t{:0.3f}\n" .format (np.max([DataIVE_SL])))
file.write("Iris Versicolor Sepal length mean:\t {:0.3f}\n" .format (np.mean([DataIVE_SL])))
file.write("Iris Versicolor Sepal Length var:\t{:0.3f}\n" .format (np.var([DataIVE_SL])))
file.write("Iris Versicolor Sepal Length StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_SL])))

file.write("Iris Versicolor Sepal Width min:\t{:0.3f}\n" .format (np.min([DataIVE_SW])))
file.write("Iris Versicolor Sepal Width max:\t{:0.3f}\n" .format (np.max([DataIVE_SW])))
file.write("Iris Versicolor Sepal Width mean:\t {:0.3f}\n" .format (np.mean([DataIVE_SW])))
file.write("Iris Versicolor Sepal Width var:\t{:0.3f}\n" .format (np.var([DataIVE_SW])))
file.write("Iris Versicolor Sepal Width StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_SW])))

file.write("Iris Versicolor PetalLengthCm min:\t{:0.3f}\n" .format (np.min([DataIVE_PL])))
file.write("Iris Versicolor PetalLengthCm max:\t{:0.3f}\n" .format (np.max([DataIVE_PL])))
file.write("Iris Versicolor PetalLengthCm mean:\t {:0.3f}\n" .format (np.mean([DataIVE_PL])))
file.write("Iris Versicolor PetalLengthCm var:\t{:0.3f}\n" .format (np.var([DataIVE_PL])))
file.write("Iris Versicolor PetalLengthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_PL])))

file.write("Iris Versicolor PetalWidthCm min:\t{:0.3f}\n" .format (np.min([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm max:\t{:0.3f}\n" .format (np.max([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm mean:\t {:0.3f}\n" .format (np.mean([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm var:\t{:0.3f}\n" .format (np.var([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_PW])))

# Dataframe sliced per species
DataIVI_SL= DataIVI["SepalLengthCm"]
DataIVI_SW= DataIVI["SepalWidthCm"]
DataIVI_PL= DataIVI["PetalLengthCm"]
DataIVI_PW= DataIVI["PetalWidthCm"]

# Export summary of variables of Iris Virginica (Data split)
file.write("Iris Virginica Attributes:\n\n")

file.write("Iris Virginica Sepal Length min:\t{:0.3f}\n" .format (np.min([DataIVI_SL])))
file.write("Iris Virginica Sepal Length max:\t{:0.3f}\n" .format (np.max([DataIVI_SL])))
file.write("Iris Virginica Sepal length mean:\t {:0.3f}\n" .format (np.mean([DataIVI_SL])))
file.write("Iris Virginica Sepal Length var:\t{:0.3f}\n" .format (np.var([DataIVI_SL])))
file.write("Iris Virginica Sepal Length StDev:\t{:0.3f}\n\n" .format (np.std([DataIVI_SL])))

file.write("Iris Virginica Sepal Width min:\t{:0.3f}\n" .format (np.min([DataIVI_SW])))
file.write("Iris Virginica Sepal Width max:\t{:0.3f}\n" .format (np.max([DataIVI_SW])))
file.write("Iris Virginica Sepal Width mean:\t {:0.3f}\n" .format (np.mean([DataIVI_SW])))
file.write("Iris Virginica Sepal Width var:\t{:0.3f}\n" .format (np.var([DataIVI_SW])))
file.write("Iris Virginica Sepal Width StDev:\t{:0.3f}\n\n" .format (np.std([DataIVI_SW])))

file.write("Iris Virginica PetalLengthCm min:\t{:0.3f}\n" .format (np.min([DataIVE_PL])))
file.write("Iris Virginica PetalLengthCm max:\t{:0.3f}\n" .format (np.max([DataIVE_PL])))
file.write("Iris Virginica PetalLengthCm mean:\t {:0.3f}\n" .format (np.mean([DataIVE_PL])))
file.write("Iris Virginica PetalLengthCm var:\t{:0.3f}\n" .format (np.var([DataIVE_PL])))
file.write("Iris Virginica PetalLengthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_PL])))

file.write("Iris Versicolor PetalWidthCm min:\t{:0.3f}\n" .format (np.min([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm max:\t{:0.3f}\n" .format (np.max([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm mean:\t {:0.3f}\n" .format (np.mean([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm var:\t{:0.3f}\n" .format (np.var([DataIVE_PW])))
file.write("Iris Versicolor PetalWidthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_PW])))

'''
###
#### Number 2: a histogram of each variable saved to png files

# need to create histograms of each variable-  x 4 for each species x 3 =12 histograms

#plt.hist(DataIS['SepalLengthCm'])
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
plt.savefig("Iris_Setosa_SepalWidth")
plt.show()
'''
# first attempt to create histograms of split data- may not be required as

#this works but look for usign a global variable for "Iris-Setosa", "Iris Virginica", "Iris Versicolor", "SepalLengthCm", 'SepalWidthCm',"PetalLengthCm","PetalWidthCm"
SL= 'SepalLengthCm'

plt.hist(DataIS[SL]) 
plt.title ("Iris-Setosa SepalLengthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Setosa_SepalLength")
plt.show()

plt.hist(DataIS['SepalWidthCm']) 
plt.title ("Iris-Setosa SepalWidthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Setosa_SepalWidth")
plt.show()

plt.hist(DataIS['PetalLengthCm']) 
plt.title ("Iris-Setosa PetalLengthCm")
plt.xlabel("Petal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Setosa_PetalLength")
plt.show()

plt.hist(DataIS['PetalWidthCm']) 
plt.title ("Iris-Setosa PetalWidthCm")
plt.xlabel("Petal Width in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Setosa_PetalWidth")
plt.show()


plt.hist(DataIVE[SL]) 
plt.title ("Iris-Versicolor_ SepalLengthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Versicolor__SepalLength")
plt.show()

plt.hist(DataIVE['SepalWidthCm']) 
plt.title ("Iris-Versicolor_ SepalWidthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Versicolor__SepalWidth")
plt.show()

plt.hist(DataIVE['PetalLengthCm']) 
plt.title ("Iris-Versicolor_ PetalLengthCm")
plt.xlabel("Petal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Versicolor__PetalLength")
plt.show()

plt.hist(DataIVE['PetalWidthCm']) 
plt.title ("Iris-Versicolor_ PetalWidthCm")
plt.xlabel("Petal Width in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Versicolor__PetalWidth")
plt.show()


plt.hist(DataIVI["SepalLengthCm"]) 
plt.title ("Iris-Versicolor_ SepalLengthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Versicolor_SepalLength")
plt.show()

plt.hist(DataIVI['SepalWidthCm']) 
plt.title ("Iris-Virginica_ SepalWidthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Virginica__SepalWidth")
plt.show()

plt.hist(DataIVI['PetalLengthCm']) 
plt.title ("Iris-Virginica_ PetalLengthCm")
plt.xlabel("Petal Length in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Virginica__PetalLength")
plt.show()

plt.hist(DataIVI['PetalWidthCm']) 
plt.title ("Iris-Virginica PetalWidthCm")
plt.xlabel("Petal Width in cm")
plt.ylabel ("Count")
plt.savefig("Iris_Virginica_PetalWidth")
plt.show()
'''


###
### Number 3:  Create correlation Visualizations

#1:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
   .add_legend()
#2:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, "SepalLengthCm", "PetalLengthCm") \
   .add_legend()
#3:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, "SepalLengthCm", "PetalWidthCm") \
   .add_legend()
#4:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, "SepalWidthCm", "PetalLengthCm") \
   .add_legend()
 #5:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, "SepalWidthCm", "PetalWidthCm") \
   .add_legend()
#6:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, "PetalLengthCm", "PetalWidthCm") \
   .add_legend()


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

'''
print ("Hello")
