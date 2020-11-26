import json
import time


with open('userdata.json', 'r') as file1:
    user_data = json.load(file1)


def start():
    print("\nHello and welcome to the loginsys, created by Banik.\n\nOptions:\n")
    print("Enter 'login' to log into your account.")
    print("Enter 'register' to create a new account.")
    print("Enter 'quit' to exit the programm.\n")

    user_input = input(": ")

    if user_input == "quit":
        exit()

    elif user_input == "login":
        login()

    elif user_input == "register":
        register()

    else:
        print("\nUnknown input!\n")

def login():
    global login_input
    login_input = input("\nEnter your account name: ")
    login_input2 = input("\nEnter your password: ")

    if login_input in user_data:
        if login_input2 == user_data[login_input]:
            logged_in()

    else:
        print("\nWrong username or password!")
        trys += 1

def logged_in():
    print("\nYour login was succesful!")

    print("\nOptions:\n")
    print("Enter 'settings' to edit your account.")
    print("Enter 'quit' to go back to the start.\n")

    user_input = input(": ")

    if user_input == "quit":
        start()

    elif user_input == "settings":
        settings()
    
    else:
        print("\nUnknown input")

def settings():
    print("\nEnter 'delete' to delete your accoun.")
    print("Enter 'name' to change the username of your account.")
    print("Enter 'password' to change the password of your account.")
    print("Enter 'quit' to back to the start section.\n")

    user_input = input(": ")

    if user_input == "quit":
        start()

    elif user_input == "delete":
        delete()
    
    elif user_input == "name":
        name()

def delete():
    print("\nDo you really want to delete your account?\n")
    print("If yes, enter 'DELETE'.\n")
    print("If not, enter 'quit' to go back to the settings menu.\n")

    user_input = input(": ")

    if user_input == "quit":
        settings()

    elif user_input == "DELETE":
        del user_data[login_input]

        print("\nYour account has been deleted.\n")
        print("Thank you for using my login/registration system.")
        print("The program will close itself automatically in five seconds.\n")

        with open('userdata.json', 'w') as outfile:
            json.dump(user_data, outfile)

        time.sleep(5)

        exit()

    else:
        print("Unknown input!")

def name():
    new_name = input("\nEnter a new username: ")
    new_name2 = input("\nConfirm your new username: ")

    if new_name == new_name2:
        user_data[new_name] = user_data[login_input]
        del user_data[login_input]

        with open('userdata.json', 'w') as outfile:
            json.dump(user_data, outfile)

        print("\nYour username was updated succesfully!")
        settings()

    else:
        print("\nInput is not matching!")

def register():
    register_input = input("\nEnter username: ")

    print("\nYour password must be minimum 4 characters long, must include a number and a special chracter ($%&!?#*).\n")
    
    register_input2 = input("Enter a password: ")
    
    if len(register_input2) >= 4 and any(c in "0123456789" for c in register_input2) and any(c in "$%&!?#*" for c in register_input2):
        if register_input not in user_data:
            user_data[register_input] = register_input2

            with open('userdata.json', 'w') as outfile:
                json.dump(user_data, outfile)

            print("\nSuccesful registration!")
            start()

        else:
            print("\nThe username is already taken!")
            
    else:
        print("\nYour password does not match the conditions!")

start()