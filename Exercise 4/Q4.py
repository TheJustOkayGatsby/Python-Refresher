
#Write a program that prompts the user for the user for their five favourite movies. Store each
#movie in a list. If the user at any stage enters Quit at any stage, the program should stop
#prompting the user for the movie name and should print to the screen the movies captured in
#the list up to that point.


list = []
print("Enter up to 5 movie names, or QUIT")

movname = input("Enter movie name: ")

while movname.lower() != "quit":
    list.append(movname)
    movname = input("Enter next movie name: ")
print("\nyour movies are as follows: ")
print(list)