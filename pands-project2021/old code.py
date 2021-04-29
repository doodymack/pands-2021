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
