import re

def username(name):
    if len(name) <6 :
       print("Invalid username. Must be 6 characters or more. ")
       exit()
    else:
         print
username_input = input("Enter a username: ")
username(username_input)

# password requirements
def hint_password(password, username):
    special_characters = re.compile('[^a-zA-Z0-9]')
    if len(password) < 9:
        print("Password must be more than 8 characters. Try another!")
        exit()
    elif len(password) > 20:
        print("Passwords must be less than 20 characters. Try again!")
        exit()
    elif any(word in password.lower() for word in ["farewill", "downham", "password", "funeral", "probate", "cremation", "job"]):
        print("You shouldn't include anything specific to Farewill in your password as it makes it easier to guess. Try again!")
        exit()
    elif username.lower() in password.lower():
        print("Your password can't contain your username! Try again!")
        exit()
    elif not any(char.isdigit() for char in password):
        print("Password must include at least one number. Try again!")
        exit()
    elif not any(char.isupper() for char in password):
        print("Password must include at least one capital letter. Try again!")
        exit()
    elif not special_characters.search(password):
        print("Password must include at least one special character. Try again!")
        exit()
    else:
        print("Success! The username and password you entered meet security criteria.")

password_input = input("Enter a password: ")
hint_password(password_input, username_input)

# ending with question to exit 
user_input = input("Do you want to exit the programme? Hit enter. ")
if user_input == (""):
    print("Thanks for using the Password Tester Tool. Let us know your feedback!" )
    exit()
