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
            print("A baby could hack this password. Password must be more than 8 characters. Try another! ")
            exit()
    elif len(password) > 20:
          print("Oh come on, now you're just showing off. Passwords must be less than 20 characters. Try again! ")
          exit()
    elif "farewill" in password.lower():
        print("Oh yeah this is a great one, nobody will guess that. NOT. Try again! ")
        exit()
    elif "downham" in password.lower():
        print("A great password! If you want to get hacked that is. Try again! ")
        exit()
    elif "password" in password.lower():
        print("You're trying to wind me up? Right? TRY AGAIN!! ")
        exit()
    elif "funeral" in password.lower():
        print("Too easy! Try again!")
        exit()
    elif "probate" in password.lower():
        print("Come on now, you know that was a bad idea! Try again!")
        exit()
    elif "cremation" in password.lower():
        print("If you were a hacker I bet this is one of the first things you'd try. (Rick Ross) Another one! ")
        exit()
    elif (username_input) in password.lower():
         print("Oh come on, you didn't seriously think that was a good password did you? ")
         exit()
    else:
          print("Success! The username and password you entered meet security criteria. Gold star for you! ")
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
     print("You didn't listen! I said enter yes or no! See ya! ")
     exit()  
