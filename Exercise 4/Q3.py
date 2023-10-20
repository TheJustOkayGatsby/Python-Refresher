#Write a program that reads three edges a, b and c for a triangle and computes the perimeter if
#the input is valid. Otherwise, display that the input is invalid. The input is valid if the sum of
#every pair of two edges is greater than the remaining edge (perimeter = a+ b +c).

print("welcome to perimeter calculation, please enter edge lengths for triangle\n")
a = float(input("please input edge a: "))
b = float(input("please input edge b: "))
c = float(input("please input edge c: "))

per = a+b+c
if a+b>c and a+c>b and b+c>a: print("\ninput is valid, and perimeter equals: " , per)
else: print("\nyour input is invalid, this is not a feasable closed triangle")