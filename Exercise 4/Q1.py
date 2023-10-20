#Create a console application which will ask the user to enter a number between 0 and 1000. The
#program will then determine if the number entered is an even number or not. If the number
#entered is an even number show the message “The number you entered is even”. If the number
#entered is an odd number show the message “The number you entered is odd”. If the user
#enters an invalid number show the message “You entered an invalid number”. In this case an
#invalid number is less than 1 or greater than 1000.

nr = float(input("please enter desired number\n"))

if nr <=1000 and nr >=1:

    if nr % 2 == 0: print("The number you entered is even")
    if nr % 2 != 0: print("The number you entered is odd")
else:
    print("you entered an invalid number")
