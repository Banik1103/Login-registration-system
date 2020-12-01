import json
import time
import hashlib


# loading usernames and passwords
with open('userdata.json', 'r') as file1:
    user_data = json.load(file1)


# entry point of my program
def start():
    print("\nHello and welcome to the loginsys, created by Banik.\n\nOptions:\n")
    print("Enter 'login' to log into your account.")
    print("Enter 'register' to create a new account.")
    print("Enter 'quit' to exit the programm.\n")

    user_input = input(": ")

    # the diffrent options
    if user_input == "quit":
        exit()

    elif user_input == "login":
        login()

    elif user_input == "register":
        register()

    else:
        print("\nUnknown input!")
        start()

# login section
def login():
    global login_input # I have to use that variable multiple times -> I'm amking it global 
    login_input = input("\nEnter your account name: ")
    login_input2 = input("\nEnter your password: ")

    if login_input in user_data:
        if hash(login_input2) == user_data[login_input]: # cheking if the hash of the input matches the hash of the stored password
            logged_in()

        else:
            print("\nWrong username or password!")
            login()

    else:
        print("\nWrong username or password!")
        login()

# I can skip that block of code, but it's here Idk y lol
def logged_in():
    print("\nYour login was succesful!")

    print("\nOptions:\n")
    print("Enter 'settings' to edit your account.")
    print("Enter 'quit' to go back to the start.\n")

    user_input = input(": ")

    # once again some options to choose from
    if user_input == "quit":
        start()

    elif user_input == "settings":
        settings()
    
    else:
        print("\nUnknown input!")
        logged_in()

# settings menu for logged in users
def settings():
    print("\nEnter 'delete' to delete your account.")
    print("Enter 'name' to change the username of your account.")
    print("Enter 'password' to change the password of your account.")
    print("Enter 'quit' to back to the start section.\n")

    user_input = input(": ")

    # once again some options to choose from
    if user_input == "quit":
        start()

    elif user_input == "delete":
        delete()
    
    elif user_input == "name":
        name()

    elif user_input == "password":
        password()

    else:
        print("\nUnknown input!")
        settings()

# the use can delete hsi acoount
def delete():
    print("\nDo you really want to delete your account?\n")
    print("If yes, enter 'DELETE'.\n")
    print("If not, enter 'quit' to go back to the settings menu.\n")

    user_input = input(": ")

    if user_input == "quit":
        settings()

    elif user_input == "DELETE":
        del user_data[login_input] # deleting the user from my database (dictionary)

        print("\nYour account has been deleted.\n")
        print("Thank you for using my login/registration system.")
        print("The program will close itself automatically in five seconds.\n")

        with open('userdata.json', 'w') as outfile:
            json.dump(user_data, outfile) # saving the new userdata wiithout the deleted user's data

        time.sleep(5)
        exit()

    else:
        print("Unknown input!")
        delete()

# the user can rename his username
def name():
    new_name = input("\nEnter a new username: ")
    new_name2 = input("\nConfirm your new username: ")

    if new_name == new_name2: # checking if the two names are the same
        user_data[new_name] = user_data[login_input] # creating a new user with a new name and old password
        del user_data[login_input] # deleting the 'old' user (-data)

        with open('userdata.json', 'w') as outfile: # storing the new username in the JSON file
            json.dump(user_data, outfile)

        print("\nYour username was updated successfully!")
        settings()

    else:
        print("\nInput is not matching!")
        name()

# the user can change his password
def password():
    new_password = input("\nEnter a new password: ")
    new_password2 = input("\nConfirm your new password: ")

    if new_password == new_password2: # checking if the two passwords are the same
        user_data[login_input] = new_password # creating a new user with a new name and old password

        with open('userdata.json', 'w') as outfile: # storing the new hash(password) in the JSON file
            json.dump(user_data, outfile)

        print("\nYour password was updated successfully!")
        settings()

    else:
        print("\nInput is not matching!")
        password()

# the user can register a new account
def register():
    register_input = input("\nEnter username: ")

    print("\nYour password must be minimum 4 characters long, must include a number and a special chracter ($%&!?#*).\n")

    register_input2 = input("Enter a password: ")
    
    # checking if the password is minimum 4 characters long and contains one digits and one special chracter
    if len(register_input2) >= 4 and any(c in "0123456789" for c in register_input2) and any(c in "$%&!?#*" for c in register_input2):
        if register_input not in user_data:
            user_data[register_input] = hash(register_input2) # storing the password's hash

            with open('userdata.json', 'w') as outfile: # storing the username and hash(password) in the JSON file
                json.dump(user_data, outfile)

            print("\nSuccessful registration!")
            start()

        else:
            print("\nThe username is already taken!")
            register()
            
    else:
        print("\nYour password does not match the conditions!")
        register()


if __name__ == "__main__":
    start()
