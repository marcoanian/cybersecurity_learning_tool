# Game Section
# ----------------------------------------Modules----------------------------------------------#
import json
import random


# ---------------------------------------Functions--------------------------------------------#

def get_valid_number(prompt):
    """
    A simple error-handling function that checks if the given input is a valid number (1, 2, or 3).
    Ensures that the user enters a valid option.

    :param prompt: A message to prompt the user for input.
    :return: A valid number (1, 2, or 3).
    """
    while True:
        x = input(prompt)
        try:
            if int(x) in [1, 2, 3]:
                return int(x)
            else:
                print("Wrong input, enter 1, 2, or 3!!!")
        except ValueError:
            print("Invalid input, please enter a number (1, 2, or 3)!")


def choose_alph():
    """
    Picks a random letter from a predefined list of alphabet letters (used for selecting data in the game).

    :return: A random letter from the alphabet list.
    """
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                     's', 't', 'u', 'v', 'w', 'y', 'z']
    return random.choice(alphabet_list)


def get_words_from_json():
    """
    Reads the glossary JSON file, selects a random word and its definition from the chosen letter section,
    and adds them to a global list. This function is used as part of the game.

    :return: A list of all words (keys) in the randomly selected section (based on the letter).
    """
    global word
    with open("glossary.json", "r") as f:
        data = json.load(f)

    # Choose a random letter to access a section in the glossary
    alpha = choose_alph()

    # Get all keys (words) from the section under the chosen letter
    key_name = [key for key in data[alpha]]

    # Randomly choose a word and its definition
    y = random.choice(key_name)
    x = data[alpha][y]

    # Store the word and its definition in a global list for the game
    word.append(y)
    word.append(x)

    return key_name


def trap_word():
    """
    Selects two 'fake' or incorrect words from the same letter section in the glossary.
    These fake words are presented as incorrect choices in the game.
    """
    global word_choice
    data = get_words_from_json()

    # Select two random fake words
    for _ in range(2):
        fake_word = random.choice(data)
        word_choice.append(fake_word)


def game_function():
    """
    The main function for running the learning game. The game presents the user with a definition,
    and the user must guess the correct word from three options (one correct and two fake).

    The game keeps track of the user's score and allows them to play multiple rounds.
    """
    global word_choice, word

    # Initialize the game score
    score = 0

    # Run the game in a loop until the user decides to quit
    while True:
        # Reset the word and word_choice lists for each round
        word = []
        word_choice = []

        # Get the word and its definition from the glossary
        get_words_from_json()
        trap_word()

        # Display the definition and present three options (one correct and two fake)
        print(f"Which key is looking for:\n{word[1]}")
        print(f"{1}: {word_choice[0]}\n{2}: {word[0]}\n{3}: {word_choice[1]}")

        # Get the user's guess
        user = get_valid_number("Enter the number of your guess: ")

        # Check if the guess is correct
        if user == 2:
            score += 1
            print(f"True!!! Your score is: {score}\n{word[0]} is the correct answer.")
        else:
            print(f"Wrong, the correct answer is: {word[0]}")

        # If the score reaches 10, ask if the user wants to continue playing
        if score == 10:
            cont_game = input(f"Your score is: {score}. Do you want to continue? (y/n): ")
            if cont_game.lower() == "n":
                print("Goodbye!")
                return
