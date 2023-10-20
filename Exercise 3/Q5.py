#Write a program that prompts the user for either 1, 2, 3 or 4.
#In your python code you will need to print out what 1, 2, 3 and 4 correspond
#to using below:
#1 = diamonds, 2= hearts, 3= clubs and 4 = spades respectively.

nr = int(input("please enter a value 1, 2, 3, or 4\n"))
if nr == 1:
    print("you've selected DIAMONDS")
elif nr == 2:
    print("you've selected HEARTS")
elif nr == 3:
    print("you've selected HEARTS")
elif nr == 4:
    print("you've selected SPADES")
else:
    print("your input was not valid, please run again")