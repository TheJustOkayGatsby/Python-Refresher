#Write a program which reads two integer values. If the first number is less than the second, print the message 
#"First number is less than the second". If the second is less than the first, print the message "Second number is less than the first". 
#If the numbers are equal, print the message "The numbers are equal"
one = input("please input first number")
two = input("please input second number")

if one>two:
  print("First number is less than the second")

elif two>one:
  print("Second number is less than the first")

elif one == two:
  print("The numbers are equal")
