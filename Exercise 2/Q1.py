#Write a program that prompts the user to enter two integer values. 
#The program then increments the first integer by 1 and calculates and 
#displays the sum of the both.
print("enter value 1, followed by 'enter'")
first = int(input())

print("enter value 2, followed by 'enter'")
second = int(input())
inc = first+1
incsum = second + inc
print("The value of first variable incremented by 1 is ", inc)
print("furthermore, the sum of this number and the second value is: " , incsum)
