# studentlist.py
#Author: PaulMcGrath
# uses built functions to create a user input database
#  asks for user to input 'what would you like to do' 
# (a) Add new student (v) View students  (q) Quit Type one letter (a/v/q):d

def displayMenu() :
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice
# test the function
var = displayMenu()
print("you chose {}".format(var))
#main program

def doAdd():
 # we fill this in later
 print("in adding")
def doView():
 # we fill this in later
 print("in viewing")
#main program
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
 if choice == 'a':
    doAdd()
 elif choice == 'v':
    doView()
 elif choice !='q':
    print("\n\nplease select either a,v or q")
 choice=displayMenu() 

 def doAdd(students):
 currentStudent = {}
 currentStudent["name"]=input("enter name :")
 currentStudent["modules"]= readModules()
 students.append(currentStudent)


def readModules():
    modules = [] #modules is an array
    moduleName = input("\tEnter the first Module name (blank to quit) :") .strip() #user inputs a module name

    while moduleName != "": #runs until blank is inputted
        module = {}  # module is a dict
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
 # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()
    return modules



#test
doAdd(students)
doAdd(students)
doAdd(students)
print (students)
