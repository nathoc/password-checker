def username(name):
    if len(name) <6 :
       print("Invalid username. Must be 6 characters or more. ")
       exit()
    else:
         print
username_input = input("Enter a username: ")
username(username_input)

# password requirements
password_input = input("Enter a password: ")
def hint_password(password):
    if len(password) < 9:
            print("Invalid password. Password must be more than 8 characters")
            exit()
    elif len(password) > 15:
          print("Invalid password. Password must be less than 15 characters")
          exit()
    elif "farewill" in password.lower():
        print("Invalid password. Password cannot contain 'Farewill'.")
        exit()
    elif "downham" in password.lower():
        print("Invalid password. Password cannot contain 'Downham'.")
        exit()
    elif "password" in password.lower():
        print("Invalid password. Password cannot contain 'Password'.")
        exit()
    elif "will" in password.lower():
        print("Invalid password. Password cannot contain 'Will'.")
        exit()
    elif "funeral" in password.lower():
        print("Invalid password. Password cannot contain 'Funeral'.")
        exit()
    elif "probate" in password.lower():
        print("Invalid password. Password cannot contain 'Probate'.")
        exit()
    elif "cremation" in password.lower():
        print("Invalid password. Password cannot contain 'Cremation'.")
        exit()
    elif (username_input) in password.lower():
         print("Invalid password. Password cannot contain username.")
         exit()
    else:
          print("The username and password you entered meet security criteria. Nice! ")
hint_password(password_input)

# ending with question to exit 
user_input = input("Do you want to exit the programme? Enter 'yes' or 'no'. ")
if user_input == ("yes"):
    print("Okay, bye!")
    exit()
if user_input == ("no"):
    print("Well, why are you still here?")
    exit()
else:
     print("I don't know what you need! ")
     exit()
