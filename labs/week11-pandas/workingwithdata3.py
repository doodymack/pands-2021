# workingwithdata3.py
#Author: PaulMcGrath
# more work om pandas - import csv  import json analysing data

import pandas as pd
import matplotlib.pyplot as plt

# import data fron comma separated file i.e.CSV into a dataframe

#df = pd.read_csv('grades.csv')

#use to_string() to print the entire DataFrame.
#print(df.to_string()) 

# print a reduced summary string i.e. if file is long prints 1st few lines then last few lines
#print(df)

# import data fron comma separated file i.e.CSV into a dataframe
df = pd.read_json('datafromW3Schools.JSON')
print(df.head(9))
#print(df.to_string()) 
#print(df.info())

# remove rows with null values -new file
#new_df = df.dropna()

# remove rows with null values -overwrite
#df.dropna(inplace = True)

#print(df.info())

#Replace all NULL values with the number 130
#df.fillna(130, inplace = True)

#Replace all NULL values in specific column "calories" with the number "130"
#df["Calories"].fillna(130, inplace = True)

# replace null values with the mean of the column (series)  can replace 'mean' with 'median' or 'mode'
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)

#to convert all cells in a 'Date' column into dates- no date format in JSON file here
#df['Date'] = pd.to_datetime(df['Date'])

#Remove rows with a NULL value in the "Calories" column:
#df.dropna(subset=['Calories'], inplace = True)

#Set "Duration" = 45 in row 7:  i.e. its 450 in JSON file but obviously a typo should be 45
#df.loc[7, 'Duration'] = 45

#Delete rows where "Duration" is higher than 120:

#for x in df.index:#
  #if df.loc[x, "Duration"] > 120:
    #df.drop(x, inplace = True)

#Returrns True for every row that is a duplicate, othwerwise False:
#print(df.duplicated())

#Remove all duplicates:
#df.drop_duplicates(inplace = True)

print(df.head(9))
print(df.info())

#Show the relationship between the columns:Note: The corr() method ignores "not numeric" columns.
print(df.corr())

# to plot data import matplotlib.pyplot as plt (see at start of file)

#df.plot()

#df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

df["Duration"].plot(kind = 'hist')




plt.show()


