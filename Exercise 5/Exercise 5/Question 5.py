#Question 5: Write the simple Calc program which is given below with option '5' to exit. Write a program which displays a menu to the user. The menu should look similar to the following:
#Welcome to the SimpleCalc
#Press 1 to add two numbers
#Press 2 to subtract two numbers
#Press 3 to divide two numbers
#Press 4 to multiple two numbers
#Read in the selection from the user and then ask the user for two numbers.
#Print the result to the user.
#Also ask the user if they want to continue or quit.(use loop)
#Using the simple calculator, create functions to perform the following:
#                Add which accepts two numbers
#                Subtract which accepts two numbers
#                Divide which accepts two numbers
#                Multiple which accepts two number

def add(x,y):
    return x+y
def subtract(x,y):
    return (x-y)
def divide(x,y):
    return (x/y)
def multiply(x,y):
    return (x*y)

def Calc():
    fn = int(input("please select desired operation,\nPress 1 to add two numbers\nPress 2 to subtract two numbers\nPress 3 to divide two numbers\nPress 4 to multiple two numbers\nPress 5 to quit\n"))
    if fn == 5:
        return (print("OPERATION ENDED"))
    x = int(input("Thank you. Please input first number for operation:"))
    y = int(input("Thank you. Please input second number for operation:"))
    endresult = float(0)
    if fn == 1:
        endresult = float(add(x,y))
    elif fn == 2:
        endresult = float(subtract(x,y))
    elif fn == 3:
        endresult = float(divide(x,y))
    elif fn == 4:
        endresult = float(multiply(x,y))
    elif fn == 5:
        print("OPERATION ENDED")
        endresult = 0

    return endresult




print(Calc())
