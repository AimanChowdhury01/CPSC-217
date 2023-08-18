#studentInfo
#Version: 23 Oct, 2022. (Parameter passing, Function return values)
#code start function
#start done, code input    
def getInput():
    number = float(input("Enter a number: "))
    return(number)
#done with input, returned function
#parameter passing for next function
def doubleIt(number):
    newNumber = number * 2
    return(newNumber)
#code of function to display output
def display(newNumber):
    print("New Number: ", end ="")
    print("%0.2f" %(newNumber))
def start():
    print("Enter a number to double it.")
    print()
    number = 0
    newNumber = 0
    number = getInput()
    newNumber = doubleIt(number)
    display(newNumber)
start()
