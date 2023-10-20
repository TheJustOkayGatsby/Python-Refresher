#Write a program in Python which prompts the user for their username in the format Domain
#Name\Username as per Figure 1a below.
#On entering their domain and username and pressing carriage return, write out to the console
#window each individual data item as per Figure 1b below.
#NOTE: The user can enter any combination of domain and username

while 1==1:
    try:
        text = input("##################################\nWELCOME TO THE DBS CONSOLE\n##################################\n Please enter your username: ")
        both = text.split('\\')
        username = both[0]
        domain = both[1]
        print("Username: ", username)
        print("Domain: " ,domain)
        break
    except:
       print("Error occurred with user input. Try again")