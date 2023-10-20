#Suppose you shop for rice in two different packages. You would like to write a program to
#compare the cost. The program prompts the user to enter the weight and price of the each
#package and displays the one with the better price.

print("welcome to cost comparison, please enter weight and price of FIRST package\n")
w1 = float(input("please enter weight in grams: "))
p1 = float(input("please enter price: "))

print("\nplease enter weight and price of SECOND package\n")
w2 = float(input("please enter weight in grams: "))
p2 = float(input("please enter price: "))

ratio1 = w1 / p1
ratio2 = w2 / p2

if ratio1 > ratio2: print("\nFIRST package is the better deal, at a price of:" , ratio1 , " grams per euro")
elif ratio2 > ratio1: print("\nSECOND package is the better deal, at a price of:" , ratio2 , " grams per euro")
elif ratio1 == ratio2: print("\nFIRST and SECOND packages are the same price per gram")

