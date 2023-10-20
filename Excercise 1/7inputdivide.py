
#7. Write a program to get the result by diving two numbers given by the user.
#Prompt the user for two values. Read the values into the console and assign to variables called num1
#and num2. Declare another variable result to store the result of dividing num1 by num2. Display the
#result


print("please input base value below and press enter")
num1 = input()
print ("you entered" , num1)

print("please input value to divide by below and press enter")
num2 = input()
print ("you entered" , num2)

result = int(num1) / int(num2) 

print("your input " , num1 , "divided by second value " , num2 , "is: " , result)
