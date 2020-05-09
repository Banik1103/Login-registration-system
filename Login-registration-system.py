import json
import time

with open("userdata.txt", "r") as file1:
    user_data = json.load(file1)

# I'm using a dictionary as a database, it stores a username and a password from a user 

# user_data = {"jeri": "1103", "hanna": "1907", "papa": "2105"}

trys = 0

while True:
    back = False
    back2 = False
    print("")
    print("Options:")
    print("")
    print("Enter 'login' to log into your account")
    print("Enter 'register' to create a new account ")
    print("Enter 'quit' to exit the programm")
    print("")
        
    user_input = input(": ") 
        
    if user_input == "quit":
        break     

    elif user_input == "login":
        while True:
            if back == True:
                break

            print("")
            print("If you typed in 'login' by mistake and want to go back to the start enter 'back'")
            print("")
            print("If you want to continue enter 'pass'")
            print("")

            login_input3 = str(input(": "))

            if login_input3 == "back":
                break

            else:
                print("")
                login_input = str(input("Enter your account name: "))  
                print("")  
                login_input2 = str(input("Enter your password: "))
            
                if login_input in user_data:
                    if login_input2 == str(user_data[login_input]):
                        print("")
                        print("Your login was succesful!")
                        trys = 0
                
                        while True:
                            print("")
                            print("Options:")
                            print("")
                            print("Enter 'settings' to edit your account")
                            print("Enter 'quit' to go back to the start")
                            print("")
                                
                            user_input3 = input(": ")
                                
                            if user_input3 == "quit":
                                back = True
                                break


                            elif user_input3 == "settings":
                                while True:
                                    print("")
                                    print("Enter 'delete' to delete your account")
                                    print("Enter 'name' to change the username of your account")
                                    print("Enter 'password' to change the password of your account")
                                    print("Enter 'quit' to back to the settings section")
                                    print("")

                                    user_input4 = input(": ")

                                    if user_input4 == "quit":
                                        break

                                    elif user_input4 == "delete":
                                            print("")
                                            print("Do you really want to delete your account?")
                                            print("")
                                            print("If yes, enter 'DELETE'")
                                            print("")
                                            print("If not, enter 'quit' to go back to the settings menu")
                                            print("")

                                            user_input5 = input(": ")

                                            if user_input5 == quit:
                                                break

                                            if user_input5 == "DELETE":
                                                del user_data[login_input]

                                                print("")
                                                print("Your account has been deleted")
                                                print("")
                                                print("Thank you for using my login system")
                                                print("")
                                                print("The program will close itself automatically in five seconds")

                                                with open('userdata.txt', 'w') as outfile:
                                                    json.dump(user_data, outfile)

                                                time.sleep(5)

                                                exit()

                                    elif user_input4 == "password":
                                        while True:
                                            print("")
                                            print("Do you really want to change your password?")
                                            print("")
                                            print("If yes, enter 'password'")
                                            print("")
                                            print("If not, enter 'quit' to go back to the settings menu")
                                            print("")

                                            user_input6 = str(input(": "))

                                            if user_input6 == "quit":
                                                break

                                            elif user_input6 == "password":
                                                print("")
                                                new_pass = str(input("Enter a new password: "))
                                                print("")
                                                new_pass2 = str(input("Confirm your new password: "))

                                                if new_pass == new_pass2:
                                                    user_data[login_input] = new_pass
                                                    print("")
                                                    print("Your password was updated succesfully")
                                                    break

                                                else:
                                                    print("")
                                                    print("Input is not matching")

                                        else:
                                            print("")
                                            print("Unknown input")

                                    elif user_input4 == "name":
                                        while True:
                                            print("")
                                            print("Do you really want to change your username?")
                                            print("")
                                            print("If yes, enter 'name'")
                                            print("")
                                            print("If not, enter 'quit' to go back to the settings menu")
                                            print("")

                                            user_input7 = str(input(": "))

                                            if user_input7 == "quit":
                                                break

                                            elif user_input7 == "name":
                                                print("")
                                                new_name = str(input("Enter a new username: "))
                                                print("")
                                                new_name2 = str(input("Confirm your new username: "))

                                                if new_name == new_name2:
                                                    user_data[new_name] = user_data[login_input]
                                                    del user_data[login_input]

                                                    print("")
                                                    print("Your username was updated succesfully")
                                                    break

                                            else:
                                                print("")
                                                print("Unknown input")

                                    else:
                                        print("")
                                        print("Unknown input!")

                            else:
                                print("")
                                print("Unknown input!")   

                    else:
                        while True:
                            print("")
                            print("Wrong username or password!")

                            trys += 1

                            if trys == 1:
                                print("")
                                print("Try again!")
                                print("")
                                print("If you fail four more times, you are not allowed to log in anymore")
                                break

                            elif trys == 2:
                                print("")
                                print("Try again!")
                                print("")
                                print("If you fail three more times, you are not allowed to log in anymore")
                                break

                            elif trys == 3:
                                print("")
                                print("Try again!")
                                print("")
                                print("If you fail two more times, you are not allowed to log in anymore")
                                break

                            elif trys == 4:
                                print("")
                                print("Try again!")
                                print("")
                                print("If you fail one more times, you are not allowed to log in anymore")
                                break

                            elif trys == 5:
                                print("")
                                print("You ran out of trys")
                                print("")
                                exit()
                                
                else:
                    while True:
                        print("")
                        print("Wrong username or password!")

                        trys += 1

                        if trys == 1:
                            print("")
                            print("Try again!")
                            print("")
                            print("If you fail four more times, you are not allowed to log in anymore")
                            break

                        elif trys == 2:
                            print("")
                            print("Try again!")
                            print("")
                            print("If you fail three more times, you are not allowed to log in anymore")
                            break

                        elif trys == 3:
                            print("")
                            print("Try again!")
                            print("")
                            print("If you fail two more times, you are not allowed to log in anymore")
                            break

                        elif trys == 4:
                            print("")
                            print("Try again!")
                            print("")
                            print("If you fail one more times, you are not allowed to log in anymore")
                            break

                        elif trys == 5:
                            print("")
                            print("You ran out of trys")
                            exit()
                
    elif user_input == "register":
            print("")
            print("If you typed in 'register' by mistake and want to go back to the start enter 'back'")
            print("")
            print("If you want to continue enter 'pass'")
            print("")

            login_input4 = str(input(": "))

            if login_input4 == "back":
                break

            else:
                print("")
                register_input = str(input("Enter username: "))
                print("")
                print("Your password must be minimum 4 characters long, must include a number and a special chracter ($%&!?#*)")
                print("")
                register_input2 = str(input("Enter a password: "))

                if len(register_input2) >= 4 and any(c in "0123456789" for c in register_input2) and any(c in "$%&!?#*" for c in register_input2):
                    if register_input not in user_data:
                        user_data[register_input] = register_input2
                        print("")
                        print("Succesful registration!")

                    else:
                        print("")
                        print("Username already taken!")
                        
                else:
                    print("")
                    print("Your password does not match the conditions!")
                
    elif user_input == "admin":
        print("")
        admin_password = str(input("Enter the admin password: ")) 
            
            
        if admin_password == "kriegst du nie!":
            print("")
            print("What is your next step? ")
                
            while True:
                print("")
                print("Enter 'user data' if you want to see secrets")
                print("Enter 'delete' to let an account disappear")
                print("Enter 'quit' to go back to the normal section")
                print("")
                    
                    
                user_input2 = input(": ")
                    
                if user_input2 == "user data":
                    print("")
                    print(user_data)     
                        
                elif user_input2 == "delete":
                    print("")
                    print("That is the list of all accounts registered:")
                    print("")
                    print(user_data)
                    print("")
                    print("Enter the username of the account you want to delete")
                    print("")

                    account_delete = str(input(": "))  

                    del user_data[account_delete]

                    print("")
                    print("The account has been removed succefully")
                    break

                elif user_input2 == "quit":
                    break       

                else:
                    print("")
                    print("Unknown input!")    
        else:
            print("")
            print("Did you just tried to get in?")
            print("Nah, not with me")

            time.sleep(2)

            exit()
    else:
        print("")
        print("Unknown input")

with open('userdata.txt', 'w') as outfile:
    json.dump(user_data, outfile)