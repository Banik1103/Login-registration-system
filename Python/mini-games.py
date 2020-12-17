import random


def start():
    print("\nHello and welcome to mini-games, the collection of small mini-games where you need luck to win the game.\nThere are 2 games (for now), the dice roler and the coin flip.\nTo play the dice roler game, enter '1', to play the coin flip game, enter '2'.\nTo quit the application, enter '10'.\n")
    return menu()

def menu():
    user_input = input(": ")

    if user_input == "1":
        return hello_1()

    elif user_input == "2":
        return hello_2()

    elif user_input == "3":
        pass

    elif user_input == "4":
        pass

    elif user_input == "10":
        exit()

    else:
        print("Unknown input, please try again.\n")
        return menu()


def hello_1():
    print("\nWelcome to the dice roler game.\nFirst you have to choose a number between 1 and 6.\nThen the dice will be rolled.\nLet's see if you can win.\n")
    print("Do you want to play?\nIf you want to, enter '1', if you want to go back to the main menu, enter '2', if you want to quit, enter '3'.\n")

    return decide()


def decide():
    user_input = input(": ")

    if user_input == "1":
        return choose()

    elif user_input == "2":
        return start()

    elif user_input == "3":
        quit()

    else:
        print("\nUnknown input, please try again.\n")
        return decide()


def choose():
    number = random.randint(1, 6)
    user_number = int(input("\nEnter your number: "))

    return roler(user_number, number)
    

def roler(user_number, number):
    if user_number == number:
        print(f"\nThe number on the dice was {number}!\nYou guessed it right!\nIf you want to play again, enter '1', if you want to go back to the main menu, enter '2', if you want to quit, enter '3'.\n")
        return decide()

    else:
        print(f"\nThe number on the dice was {number}!\nAh, you didn't get it right!\nIf you want to play again, enter '1', if you want to go back to the main menu, enter '2', if you want to quit, enter '3'.\n")
        return decide()


def hello_2():
    print("\nWelcome to the coin flip game.\nFirst you have to choose heads or tails.\nThen the coin will be flipped.\nLet's see if you can win.\n")
    print("Do you want to play?\nIf you want to, enter '1', if you want to go back to the main menu, enter '2', if you want to quit, enter '3'.\n")

    return decide_2()


def decide_2():
    user_input = input(": ")

    if user_input == "1":
        return choose_2()

    elif user_input == "2":
        return start()

    elif user_input == "3":
        quit()
    
    else:
        print("\nUnknown input, please try again.\n")
        return decide_2()


def choose_2():
    number = random.choice(["head", "tail"])
    user_guess = str(input("\nEnter 'heads' or '1' for heads or 'tails' or '2' for tails: "))
    user_number = 0

    if "heads" in user_guess or "1" in user_guess: 
        user_number = 1
    
    elif "tails" in user_guess or "2" in user_guess:
        user_number = 2
    
    else:
        print("\nUnknown input, please try again.\n")
        return choose_2()

    return coin_flip(number, user_number)


def coin_flip(number, user_number):
    if user_number == number:
        print(f"\nThe coin says: {number}!\nYou guessed it right!\nIf you want to play again, enter '1', if you want to go back to the main menu, enter '2', if you want to quit, enter '3'.\n")
        return decide_2()

    else:
        print(f"\nThe coin says: {number}!\nAh, you didn't get it right!\nIf you want to play again, enter '1', if you want to go back to the main menu, enter '2', if you want to quit, enter '3'.\n")
        return decide_2()


if __name__ == "__main__":
    start()