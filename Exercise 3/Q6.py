#Write a program which displays a menu to the user. 
#The menu should look similar to the following:

#Welcome to the SimpleCacl
#Press 1 to add two numbers
#Press 2 to subtract two numbers
#Press 3 to divide two numbers
#Press 4 to multiple two numbers

#Read in the selection from the user and then ask the user for two numbers.
#Print the result to the user

fn = int(input("#Welcome to the SimpleCacl\nPress 1 to add two numbers\nPress 2 to subtract two numbers\nPress 3 to divide two numbers\nPress 4 to multiply two numbers\n"))
if fn == 1: print("you've selected ADD")
elif fn == 2: print("you've selected SUBTRACT")
elif fn == 3: print("you've selected DIVIDE")
elif fn == 4: print("you've selected MULTIPLY")

one = float(input("please enter first value: "))
two = float(input("please enter second value: "))
result = float()

if fn == 1:
    result = one + two
    print(one , "ADDED to" , two , "is EQUAL to" , result)
elif fn == 2:
    result = one - two
    print(one , "MINUS " , two , "is EQUAL to" , result)
elif fn == 3:
    result = one / two
    print(one , "DIVIDED by" , two , "is EQUAL to" , result)
elif fn == 4:
    result = one * two
    print(one , "MULTIPLIED by" , two , "is EQUAL to" , result)

