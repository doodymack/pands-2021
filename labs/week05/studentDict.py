# studentDict.py
#Author: Paul Mc Grath
# a program that stores
# a student name 
# a list of his/her courses and grades in a dict.
# The program should then print out his/her data.
# The number of course she has could change

student = { 
    "name": "Mary", 
    "modules": [
        {
            "courseName":"Programming",
            "grade": 63         
        },
        {
            "courseName":"Computer Architecture",
            "grade": 74
        },     
        {
            "courseName":"Applied Databases",
            "grade": 80
        }, 
         {
            "courseName":"Web Applications Development",
            "grade": 90
        },  
        {
            "courseName":"Computational Thinking with Algorithms",
            "grade": 55
        } 
    ]
}
print ("Student: {}".format(student ["name"]))

for module in student["modules"]:
   print("\t {} \t: {}".format(module["courseName"], module["grade"]))




