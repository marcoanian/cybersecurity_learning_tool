# A Command Line Interface to learn and search for terms, related to "Google Cybersecurity Certificate"
# Date: 06.09.2024
# Version 1.0, Created by Marco Anian

# ----------------------------------------Imported Modules----------------------------------------#
from main_cli import search_tool
from game import game_function, get_valid_number


# ----------------------------------------Main Function--------------------------------------------#
def google_cyber_security_game():
    """
    The main function that runs the command-line interface for the Google Cybersecurity Certificate learning tool.

    This tool allows users to:
    1. Search for terms in the glossary.
    2. Play a learning game where definitions are provided, and users guess the correct terms.
    3. Exit the application.

    The user will be prompted to choose between these options repeatedly until they decide to exit.
    """

    # Welcome and instructions
    print("A Command Line Interface to learn and search for terms related to the 'Google Cybersecurity Certificate'")
    print("Release: 10.09.2024, Version 1.0, Created by Marco Anian\n")
    print("Welcome to this learning tool for Google cybersecurity terms and definitions. Here are your options:")
    print(
        "1 - Search data: Look up glossary terms or search by keywords. Shows all keywords if the search term is not found.")
    print("2 - Game: A fun game where a definition is shown, and you choose the correct keyword from three options.")
    print("3 - Exit: Exit the application.\n")

    # Main loop to keep the program running until the user decides to exit
    while True:
        # Ask the user to choose an option
        user_input = get_valid_number("1 for search data, 2 for game, 3 for Exit: ")

        # Option 1: Search tool
        if user_input == 1:
            search_tool()

        # Option 2: Game function
        elif user_input == 2:
            game_function()

        # Option 3: Exit the application
        elif user_input == 3:
            print("Thank you for using the Google Cybersecurity Certificate learning tool. Goodbye!")
            return  # Exits the application


# --------------------------------------------Run the Application--------------------------------------------#
# Call the main function to start the tool
google_cyber_security_game()
