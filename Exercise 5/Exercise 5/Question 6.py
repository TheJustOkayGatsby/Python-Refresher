#The program requires the clerk to enter the following information:
#·How many miles must the item be transported?
#·What is the weight of the items being transported?
#·Is this a regular customer?
#The program should then display the Total amount for the bill. 
#If a discount was applied show how much the value of the discount is. 
#Write appropriate functions to calculate the each cost. 
#Then add the cost to calculate total bill
def distancecost(dist):
    if dist <= 100:
        return dist * .5
    elif dist > 100 and dist <=200:
        dist -= 100
        total = float(dist*.4)
        return total + 50
    elif dist > 200:
        dist -= 200 
        total = float(dist*.3)
        return total + 90

def weightcost(weight):
    if weight <= 100:
        return weight * .33
    elif weight > 100 and weight <=200:
        weight -= 100
        total = float(weight*.23)
        return total + 33
    elif weight > 200:
        weight -= 200 
        total = float(weight*.17)
        return total + 56

def rcdiscount(x):
    discount = float(x*.075)
    return discount

def PriceScheme():
    mi = float(input("How many miles must the item be transported?\n"))
    kg = float(input("What is the weight of the items being transported in kg?\n"))
    rc = input("Is this a regular customer? (y/n)\n")
    if rc.lower() == "yes" or rc.lower() == "y":
        rc = bool(0)
    elif rc.lower() == "no" or rc.lower() == "n":
        rc = bool(1)
    else:
        print("Value for regular customer not valid input") 

    baseprice = float(weightcost(kg)+distancecost(mi))
    print("Total price for given transport is: " , baseprice)
    if rc == 0: 
        discount = float(rcdiscount(baseprice))
        totalprice = baseprice-discount
        print("Less the customer discount of:" , discount , "\n\nComes to a grand total of:" , totalprice)
    

PriceScheme()