#6. Write a program to get the result by adding two integers given by the user.
#Prompt the user for two integer values. Read the values into the console and assign to variables
#called num1 and num2. Declare another variable sum to store the result of adding two numbers.
#Display the result.




print("please input first value below and press enter")
basevalue = input()
print ("you entered" , basevalue)

print("please input second value to add to original value below and press enter")
secvalue = input()
print ("you entered" , secvalue)

sum = int(basevalue)+int(secvalue) 

print("your input " , basevalue , "along with second value " , secvalue , "sums to: " , sum)
