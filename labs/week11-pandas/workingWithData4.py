#workingWithData4.py
# Author: PaulMcGrath

# Load a Python Dictionary within the file into a DataFrame:



import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
# df = pd.DataFrame(data, index = ["day1", "day2", "day3","day4","day5"]) this gives NaN for all values?
# df = pd.DataFrame(data, index = {"day1", "day2", "day3","day4","day5"}) this gives NaN for all values?

#print(df) 
# head(x): print 1st (x) lines including the column(series) titles. 
# if the number of rows is not specified, the head() method will return the top 5 rows inc header.
# can use same method ansd tail() from bottom of dataframe
print(df.head())
#print(df.tail(1))

# Print information about the data:
print(df.info())