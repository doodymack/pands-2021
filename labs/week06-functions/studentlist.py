# studentlist.py
#Author: PaulMcGrath
# uses built functions to create a user input database
#  asks for user to input 'what would you like to do' 
# (a) Add new student (v) View students  (q) Quit Type one letter (a/v/q):d

def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
 modules = []
 moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

 while moduleName != "":
    module = {}
    module["name"]= moduleName
    # I am not doing error handling
    module["grade"]=int(input("\t\tEnter grade:"))
    modules.append(module)
    # now read the next module name
    moduleName = input("\tEnter next module name (blank to quit) :").strip()
 return modules

def doView(students):
 # we fill this in later
 print(students)

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()