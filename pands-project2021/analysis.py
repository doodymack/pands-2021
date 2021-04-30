# analysis.py
# Author: paul mcgrath


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("iris.csv" ,header=0)


file = open("SummaryOfEachVariable.txt" ,"w")

### Number 1:  a summary of each variable outputted to a single text file (append)

species_list = list(data["Species"].unique())

file.write("\nTypes of species: \n{}\n". format(species_list))

file.write("Dataset length: \t{}\n\n" . format (len(data)))


SL= "SepalLengthCm"
SW ="SepalWidthCm"
PL= "PetalLengthCm"
PW= "PetalWidthCm"

file.write("Sepal length range: \t[{}, {}]\n" .format (min(data[SL]) , max(data[SL])))
file.write("Sepal width range:  \t[{}, {}]\n" .format (min(data[SW]), max(data[SW])))
file.write("Petal length range: \t[{}, {}]\n" .format (min(data[PL]), max(data[PL])))
file.write("Petal width range:  \t[{}, {}]\n" .format (min(data[PW]), max(data[PW])))

file.write("Sepal length mean:\t {:0.3f}\n" .format ( np.mean(data[SL])))
file.write("Sepal width mean: \t {:0.3f}\n"  .format( np.mean(data[SW])))
file.write("Petal length mean:\t {:0.3f}\n"  .format ( np.mean(data[PL])))
file.write("Petal width mean: \t {:0.3f}\n" .format ( np.mean(data[PW])))

file.write("Sepal length variance:\t {:0.3f}\n" .format ( np.var(data[SL])))
file.write("Sepal width variance: \t {:0.3f}\n"  .format( np.var(data[SW])))
file.write("Petal length variance:\t {:0.3f}\n"  .format ( np.var(data[PL])))
file.write("Petal width variance: \t {:0.3f}\n"  . format ( np.var(data[PW])))

file.write("Sepal length StDev:\t {:0.3f}\n" .format (np.std(data[SL])))
file.write("Sepal width StDev: \t {:0.3f}\n" .format  (np.std(data[SW])))
file.write("Petal length StDev:\t {:0.3f}\n" .format  (np.std(data[PL])))
file.write("Petal width StDev: \t {:0.3f}\n\n" . format (np.std(data[PW])))

# Dataframe sliced per species
DataIS = (data.loc[data["Species"]=="Iris-setosa"])
DataIVE = (data.loc[data["Species"]=="Iris-versicolor"])
DataIVI = (data.loc[data["Species"]=="Iris-virginica"])


file.write("Iris Setosa Attributes:\n")
file.write("************************\n")

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


DataIVE_SL= DataIVE["SepalLengthCm"]
DataIVE_SW= DataIVE["SepalWidthCm"]
DataIVE_PL= DataIVE["PetalLengthCm"]
DataIVE_PW= DataIVE["PetalWidthCm"]


# Export summary of variables of Iris Versicolor (Data split)
file.write("Iris Versicolor Attributes:\n")
file.write("***************************\n")

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


DataIVI_SL= DataIVI["SepalLengthCm"]
DataIVI_SW= DataIVI["SepalWidthCm"]
DataIVI_PL= DataIVI["PetalLengthCm"]
DataIVI_PW= DataIVI["PetalWidthCm"]

# Export summary of variables of Iris Virginica (Data split)
file.write("Iris Virginica Attributes:\n")
file.write("**************************\n")

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

file.write("Iris Virginica PetalWidthCm min:\t{:0.3f}\n" .format (np.min([DataIVE_PW])))
file.write("Iris Virginica PetalWidthCm max:\t{:0.3f}\n" .format (np.max([DataIVE_PW])))
file.write("Iris Virginica PetalWidthCm mean:\t {:0.3f}\n" .format (np.mean([DataIVE_PW])))
file.write("Iris Virginica PetalWidthCm var:\t{:0.3f}\n" .format (np.var([DataIVE_PW])))
file.write("Iris Virginica PetalWidthCm StDev:\t{:0.3f}\n\n" .format (np.std([DataIVE_PW])))


# a histogram of each variable saved to png files

plt.hist(DataIS[SL]) 
plt.title ("Iris-Setosa SepalLengthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIS[SL].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Setosa_SepalLength")
plt.show()

plt.hist(DataIS[SW]) 
plt.title ("Iris-Setosa SepalWidthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIS[SW].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Setosa_SepalWidth")
plt.show()

plt.hist(DataIS[PL]) 
plt.title ("Iris-Setosa PetalLengthCm")
plt.xlabel("Petal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIS[PL].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Setosa_PetalLength")
plt.show()

plt.hist(DataIS[PW])
plt.title ("Iris-Setosa PetalWidthCm")
plt.xlabel("Petal Width in cm")
plt.ylabel ("Count")
plt.axvline(DataIS[PW].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Setosa_PetalWidth")
plt.show()


plt.hist(DataIVE[SL]) 
plt.title ("Iris-Versicolor_ SepalLengthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIVE[SL].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Versicolor__SepalLength")
plt.show()

plt.hist(DataIVE[SW]) 
plt.title ("Iris-Versicolor_ SepalWidthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIVE[SW].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Versicolor__SepalWidth")
plt.show()

plt.hist(DataIVE[PL]) 
plt.title ("Iris-Versicolor_ PetalLengthCm")
plt.xlabel("Petal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIVE[PL].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Versicolor__PetalLength")
plt.show()

plt.hist(DataIVE[PW]) 
plt.title ("Iris-Versicolor_ PetalWidthCm")
plt.xlabel("Petal Width in cm")
plt.ylabel ("Count")
plt.axvline(DataIVE[PW].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Versicolor__PetalWidth")
plt.show()

plt.hist(DataIVI[SL]) 
plt.title ("Iris-Virginica_ SepalLengthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIVI[SL].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Virginica_SepalLength")
plt.show()

plt.hist(DataIVI[SW]) 
plt.title ("Iris-Virginica_ SepalWidthCm")
plt.xlabel("Sepal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIVI[SW].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Virginica__SepalWidth")
plt.show()

plt.hist(DataIVI[PL]) 
plt.title ("Iris-Virginica_ PetalLengthCm")
plt.xlabel("Petal Length in cm")
plt.ylabel ("Count")
plt.axvline(DataIVI[PL].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Virginica__PetalLength")
plt.show()

plt.hist(DataIVI[PW]) 
plt.title ("Iris-Virginica PetalWidthCm")
plt.xlabel("Petal Width in cm")
plt.ylabel ("Count")
plt.axvline(DataIVI[PW].mean(), color='r', linestyle='dashed', linewidth=1)
plt.legend("M")
plt.savefig("Iris_Virginica_PetalWidth")
plt.show()


# Number 3:  Create correlation Visualizations

#1:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, SL, SW) \
   .add_legend()
plt.show()

#2:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, SL, PL) \
   .add_legend()
plt.show()

#3:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, SL, PW) \
   .add_legend()
plt.show()

#4:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, SW, PL) \
   .add_legend()
plt.show()

 #5:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, SW, PW) \
   .add_legend()
plt.show()

#6:
sns.FacetGrid(data, hue="Species", palette="hls", size=5) \
   .map(plt.scatter, PL, PW) \
   .add_legend()
plt.show()

