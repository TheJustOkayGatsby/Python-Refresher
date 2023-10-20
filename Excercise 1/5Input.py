
#5. Write a program to accept a numeric input from the user.
#The program prompts the user to enter an integer value.
#Read the value input, increment by 1 and output to result the user.

print("please input value to add +1 to below and press enter")
value = input()
print ("you entered" , value)
valueup = int(value)+1 #for some reason int(valueup) = int(value)+1 did not work. Why?
print("your input " , value , "with 1 added to it is:" , valueup)