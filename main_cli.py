# ------------------------------------------------Imported Modules----------------------------------------#
import json
import random
from error_handlings import get_valid_string, get_valid_num  # Custom error handling functions

# ------------------------------------------------Constants---------------------------------------------#
WORDS = {}  # Dictionary to store searched words for later saving


# ----------------------------------------------Functions------------------------------------------------#

def search_json(term):
    """
    Search for a term in the glossary JSON file and return the definition if found.
    Stores the found term and definition in the global WORDS dictionary.

    :param term: The word to search for.
    :return: The definition of the term if found, otherwise prints available terms or error message.
    """
    global WORDS
    term = term.lower()  # Convert input to lowercase to ensure case-insensitive matching
    try:
        # Open the glossary JSON file
        with open("glossary.json", "r") as file:
            data = json.load(file)  # Load JSON data
            letter = term[0]  # Get the first letter of the term to find its section in the JSON
            if letter in data:
                if term in data[letter]:
                    # Add found term and its definition to WORDS dictionary
                    WORDS[term] = data[letter][term]
                    return data[letter][term]  # Return the definition
                else:
                    print(f"Term not found. Available terms in '{letter}' section: {list(data[letter].keys())}")
            else:
                print("No section found for the entered term.")
    except FileNotFoundError:
        print("File not found, check name or file in directory!!!")


def glossary_json(term):
    """
    Get the list of all available terms in a specific section of the glossary (based on the first letter).

    :param term: The first letter to search in the glossary (a, b, c...).
    :return: List of all terms starting with the given letter, or an error message if not found.
    """
    term = term.lower()  # Convert input to lowercase for consistency
    try:
        # Open the glossary JSON file
        with open("glossary.json", "r") as file:
            data = json.load(file)  # Load JSON data
            letter = term  # Set the first letter to search in the glossary
            if letter in data:
                return list(data[letter].keys())  # Return a list of all available terms in that section
            else:
                print(f"No section found for the entered term '{letter}'.")
    except FileNotFoundError:
        print("File not found, check name or file in directory!!!")


def savefile():
    """
    Save the words searched so far (stored in WORDS) to a text file named 'memories_word.txt'.
    """
    global WORDS
    with open("memories_word.txt", "a") as f:
        # Write each term and its definition into the file
        for key in WORDS.keys():
            data = f"{key} | {WORDS[key]}\n"
            f.write(data)
        print("file saved to text!!!")


# ----------------------------------------------CLI-------------------------------------------------------#

def search_tool():
    """
    Main command-line interface (CLI) function for interacting with the user.
    Allows the user to search the glossary by first letter or by full word and saves searched terms if requested.
    """
    global WORDS
    # Greeting and user options
    print("Welcome to learning tool, for Cybersecurity")
    while True:
        # Ask user if they want to search the glossary by letter or by word
        user_choice = get_valid_num("For Glossary enter 1, for Search by name enter 2: ")
        if user_choice == 1:
            # Glossary search by first letter
            term = get_valid_string("Enter the first letter (like a or b): ")
            response = glossary_json(term)
            print(response)
        else:
            # Search by specific word
            term = get_valid_string("Enter the word you are looking for (like bit): ")
            response = search_json(term)
            print(response)

        # Ask if the user wants to continue or exit
        user_continue = get_valid_num("1 for continue, 2 for exit: ")
        if user_continue == 2:
            # If the user chooses to exit, ask if they want to save the searched terms
            safe_words = get_valid_string("Do you want to save the words to txt? (y or n): ")
            if safe_words == "y":
                savefile()
                return
            else:
                print("Goodbye!")
                return
