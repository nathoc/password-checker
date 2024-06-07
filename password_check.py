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
    elif "downham" in password.lower()
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
    else:
          print("The username and password you entered meets all of the arguments,yay! ")
hint_password(password_input)

# ending with question to exit 
continue_now = input("Do you want to exit? Hit enter. ")
print("Thanks for using the Password Checker tool. ")

# test 23

# testing