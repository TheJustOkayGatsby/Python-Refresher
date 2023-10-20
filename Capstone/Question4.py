#Implement the MYPY Phone Book System in Python as per Figure 3 below which allows
#users to add, delete, update and lookup phone numbers. The MYPY Phone Book System
#should store the individual’s Full Name and Phone Number. Your program should not allow
#users to add the same number twice. On adding, deleting, updating or looking up a number,
#your program should let the user know if the operation was successful or not. On looking up
#a number return the full name and number of the individual; if the number is not found give
#the user the option to add the details they are looking up. The user can perform multiple
#actions; they can add a new entry and subsequently delete an entry without having to stop and
#start the program until they decide to quit.
def welcome():
    print("\n1 : Add New Entry")
    print("2 : Delete Entry")
    print("3 : Update Entry")
    print("4 : Lookup Number")
    print("5 : QUIT")
print("##################################\nMYPY PHONE BOOK\n##################################")
book = {}
def add(number, name):
    book.update(
        {number : name}
        )


def onetofive():
    x = int(8675309)
    while True:
        if x == 1 or x == 2 or x==3 or x==4 or x==5:
            return x
            break
        elif x == 8675309:
            print("Welcome. Please enter a value 1-5:")
            welcome()
            while True:
                try:
                    x = int(input())
                    break
                except:
                    print("invalid value. try again")

        elif x != 1 or x != 2 or x != 3 or x != 4 or x != 5:
            print("Try again. Please enter a value 1-5:")
            while True:
                try:
                    x = int(input())
                    break
                except:
                    print("invalid value. try again")

            


def run():
    x = onetofive()
    while x != 5:
        while x == 1:
            while True:
                try:
                    number = input("Please enter phone number to add: ")
                    break
                except:
                    print("Invalid value. Try again")
            while True:
                try:
                    name = input("Please enter name associated with this number")
                    break
                except:
                    print("Invalid value. Try again")
            
            if number in book:
                print("It appears that the number already exists in the phonebook, please try again.")
                x = onetofive()
            elif number not in book:
                add(number,name)
                print("The entry has been created")
                x = onetofive()

        while x == 2:
            while True:
                try:
                    number = input("Please enter phone number to delete: ")
                    break
                except:
                    print("Invalid value. Try again")            
            if number in book:
                book.pop(number)
                print("Number deleted.")
                x = onetofive()
            if number not in book:
                print("The entry was not present in phonebook. No action has occured.")
                x= onetofive()

        while x ==3:
            while True:
                try:
                    updnumber = input("Please enter phone number to update: ")
                    break
                except:
                    print("Invalid value. Try again")            
            if updnumber in book:
                print("The number exists in the phonebook. Enter updated information")
                while True:
                    try:
                        newnumber = input("Please enter updated number: ")
                        break
                    except:
                        print("Invalid value. Try again")      
                while True:
                    try:
                        newname = input("Please enter updated name: ")
                        break
                    except:
                        print("Invalid value. Try again") 
                book.pop(updnumber)
                add(newnumber, newname)
                print("Entry updated with new name and number")
                x = onetofive()
            elif number not in book:
                while True:
                    try:
                        name = input("The entry does not yet exist. Please type a name to add to entry: ")
                        break
                    except:
                        print("Invalid value. Try again")  
                add(number,name)
                x = onetofive()

        while x ==4:
            while 1==1:
                try:
                    terms = input("Please enter number to search for: ")
                    break
                except:
                    print("Unrecognized value. Please try again")
                    
            if terms in book:
                search = [terms]
                print(f'{terms} found in phonebook.\nNumber: {terms}\nName: {book[terms]}')
                welcome()
                x = int(input())
            elif terms not in book:
                name = input("The entry does not yet exist. Would you like to add it? Please type a name to add to entry or 'NO' to continue: ")
                if name != "NO".lower():
                    add(terms,name)

                welcome()
                x = int(input())
                 
    print("QUIT, press any key to continue")
run()