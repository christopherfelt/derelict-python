import time

import help
import archive
import procedure

def main():
    print("Power levels critically low...")
    time.sleep(1)
    print("Acessing auxiliary power ... please wait")
    time.sleep(1)
    
    loadingAnimation()
    userInputDispatch()
    
    
def loadingAnimation():
    dots = "."
    
    n = 0
    while n < 5:
        print(dots, end="", flush=True)
        n += 1
        time.sleep(.25)

def userInputDispatch():
    exit = False
    
    while exit != True:
        userInput = getUserInput()
        userInput = userInput.split()
        if userInput[0] == "help":
            help.mainHelpMenu()
        elif userInput[0] == "archive":
            archive.archiveDispatch()
        elif userInput[0] == "exit":
            print("Bye")
            exit = True
        
        

def getUserInput():
    print()
    return input("> ")




if __name__ == "__main__":
    main()