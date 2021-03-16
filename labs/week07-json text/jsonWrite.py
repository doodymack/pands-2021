# jsonWrite.py
#Author: PaulMcGrath
## messing with json

# when I called file json.py got an error.  AttributeError: 'module' object has no attribute 'dumps' 
# changed it to json Write.py. Works fine.  json.py likely a module which confuses

import json

filename="testdict.json"
sample= dict(name='fred' " " "zimmermann", age=1000000.1, grades=[1,34,55])
# tried to write dict object with age=B   'error name 'B' is not defined. 
# Variable 'age' expects a number
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

#test the function

writeDict(sample)