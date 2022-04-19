#!/usr/bin/env python3
"""
Huntdown Tally Counter:
George Wiseman
2022
"""


from typing import Dict

def handle_yn_input(message:str) -> bool:
    """
    Prompts the user with a question that they can answer yes ('y') or
    no ('n') to. Returns their answer as a boolean value.
    If their answer is not valid, they will be reprompted.
    Parameters:
    - message:str A string message that will be displayed as a question for
                 the user to answer
    Return Value:
    - True when the user inputs 'y'
    - False when the user inputs 'n'
    """
    answer = input(message)
    while(True):
        try:
            if answer.lower().strip() == "y":
                return True
            elif answer.lower().strip() == "n":
                return False
            else:
                print("")
                answer = input("That is not valid y or n... \n" + message)
        except:
            print("")
            answer = input("That is not valid y or n... \n" + message)

def handle_int_input(message:str) -> int:
    """
    Prompts the user to han
    Parameters:
    - message:str A string message that will be displayed as a question for
                 the user to answer
    Return Value:
    - True when the user inputs 'y'
    - False when the user inputs 'n'
    """
    answer = input(message)
    while(True):
        try:
            answer = int(answer)
            return answer
        except:
            print("\nNot a valid number")
            answer = input(message)


def create_cabin_dict () -> dict:
    """
    Handles the input phase for creating the dictionaries for this game.
    Users will be prompted to input cabin names, and asked if they
    would like to continue inputting more, or if they are completed.
    """
    add_cabin_bool = True
    cabin_dict = {}
    while add_cabin_bool:
        cabin_name = input("Type Cabin Name: ")
        cabin_dict[cabin_name] = 0
        print("")
        add_cabin_bool = handle_yn_input("Add another cabin? Type y/n: ")
        print("")

    return cabin_dict


def input_points () -> dict:
    """
    Handles running and calculating the scores for the game. Users will
    be guided through entering all the cabins and then guided through
    inputting all the tally sheets and the number of tallies per cabin.
    Once the user indicates they are done, the final scores will be displayed.
    No paramters or return values. Users are guided throught the steps using stdout.
    """
    cabin_dict = create_cabin_dict () #Guide the user through setting up cabins
    add_another = True
    print("Get the first staff sheet out")
    # Loop through adding more staff sheets until the user indicates they
    # are done.
    while add_another:
        staff_points = handle_int_input("How many points is this staff worth? Type a number: ")
        print("")
        for cabin in cabin_dict:
            print("\nThis is for the cabin called: " + cabin)
            tags = handle_int_input("How many times did this cabin tag the staff? Type a number: ")
            total_points = tags * staff_points
            cabin_dict[cabin] += total_points
            print("")
        print("Current point layout: ", cabin_dict)
        add_another = handle_yn_input("Add another staff tally sheet? Type y/n: ")
        print("")

    # All sheets are added, now print the final scores
    print("Final Scores Are:")
    for cabin in cabin_dict:
        print(cabin, str(cabin_dict[cabin]))

def main():
    """
    The main entry point of this program
    """
    print("\nWelcome to the Huntdown Tally Counter!")
    print("by George Wiseman")
    print("\n\nYou will be guided through the steps for inputting all the staff points from the game.\n\n")

    input_points()

if __name__ == "__main__":
    main()
