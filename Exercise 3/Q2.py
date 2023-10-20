#Write a program that prompts the user to enter age. If age of the user is equal to or greater than 18, 
#then the proram displays “You are eligibel to vote”. Otherwise the program displays “You cannot vote”.

age = input("please enter age")
if age >=18:
  print("You are eligibel to vote")
elif age<18:
    print("You cannot vote")