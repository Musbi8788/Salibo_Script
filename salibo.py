"""
Salibo Script 
-----------------
A simple program that gives you salibo (Eid money) based on the length of your name.
User data is stored in a JSON file.
"""

import json

SALIBO_AMOUNT = 50


def get_stored_user():
    """_summary_

    Returns:
        _type_: _Get the user name in from the json file_
    """
    try:
        filename = 'salibo.json'
        with open(filename, encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user():
    """Get new user and store it in the json file"""
    filename = 'salibo.json'
    username = input("What's your name: ")
    if username:
        with open(filename, 'w', encoding="utf-8") as file_object:
            json.dump(username, file_object)

        return username


def give_user_salibo():
    """Give the user's salibo"""
    username = get_stored_user()
    if username:
        verify_name = input(
            f"\nIs this your name {username}\nType 'yes' or 'no': ")
        if verify_name == 'yes':
            salibo_money = len(username) * SALIBO_AMOUNT
            print(
                f"\nHappy Eid {username.title()} and your salibo money is D{salibo_money}")
        elif verify_name == 'no':
            username = get_new_user()
            salibo_money = len(username) * SALIBO_AMOUNT
            print(
                f"\nHappy Eid {username} and your salibo money is D{salibo_money}")
            
        else:
            print(f"\nInvalid input: {verify_name} please type 'yes' or 'no'.")

    else:
        username = get_new_user()
        print(
            f"\nI'll remember you when you come back, {username} and tell you your salibo.")


if __name__ == "__main__":
    while True:
        print("\nWelcome to salibo script.")
        action = input("Type 'c' to continue or 'q' to exit: ").lower()
        if action == 'c':
            give_user_salibo()
        elif action == 'q':
            break
        else:
            print("Invalid input: hint| type 'c' or 'q' ")


