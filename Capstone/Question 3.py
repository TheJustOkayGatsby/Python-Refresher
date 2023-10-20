#Write a program in Python that prompts the user to enter a number of integer values. The
#program stores the integers, counts the frequency of each integer and displays the frequency
#as per Figure 2 below.
from collections import Counter

print("##################################\nWELCOME TO THE DBS CONSOLE\n##################################")
length = int()
count = 0
elements = []

while 1==1:
    try:
        length = int(input("Please enter the number of elements to be stored in the list:"))
        break
    except:
        print("Invalid value, please try again.")

while count != length:
    print("element - " , count, ": ")
    while 1==1:
        try:
            elements.append(int(input()))
            break
        except:
            print("Invalid value, please try again.")
    count = count+1

count = 0
unique = []
print("The frequency of all elements of the list :")
for number in elements:
        if number not in unique:
            unique.append(number)

while count != len(unique):
    temp = unique[count]
    print(temp, "appears" , elements.count(temp), "times")
    count = count +1