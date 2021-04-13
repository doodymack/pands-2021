# weekday.py
# author: Psul Mc Grath
# simple programe that reads in the date
# if its a weekday it prints one command
# if its Sat or Sun it prints out another command
# simple if else
# found some options on stackoverflow:  
# https://stackoverflow.com/questions/45870820/how-to-check-if-today-is-monday-in-python
# https://www.w3schools.com/python/python_datetime.asp

from datetime import date

if date.today().weekday() == 0:
    print ("Horrah its the weekend!")
else:
    print ("Yes, unfortunately today is a weekday")
print ("By the way its {} today".format (date.today()))  

