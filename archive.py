import cl_utility

def mainArchiveMenu():
    print("Choose one of the following:")
    print("Personnel")
    print("Departments")
    print("")
    
def archiveDispatch():
    print("**Archive**")
    mainArchiveMenu()
    
    exit = False
    while exit < 5:
        userInput = cl_utility.getUserInput()
        if userInput[0].lower() == "personnel":
            personnelDispatch()
        elif userInput[0] == "exit":
            exit = True
        else:
            print("Sorry that command could not be proccessed")
        
        
def personnelDispatch():
    print("Please enter a name")
    userInput = cl_utility.getUserInput()
    records = personnelRecords()
    selected = [x for x in records if x["name"] == userInput[0]][0]
    print(selected)
    
    
    

def personnelRecords():
    return [
        {"name": "bob", "age": 48, "sex": "m"},
        {"name": "sally", "age": 45, "sex": "f"}
        
    ]
    
def personnelRecordForm():
    print()