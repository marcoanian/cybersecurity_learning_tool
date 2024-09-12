# Error Handling module

def get_valid_string(prompt):
    """
    Asks the user for a string input and ensures the input contains only letters.
    If the user enters a non-letter character (like a number), the function will prompt them again.

    :param prompt: The message to show when asking for input.
    :return: The valid input string converted to lowercase.
    """
    while True:
        x = input(prompt).lower()  # Convert the input to lowercase
        try:
            # Try converting the input to an integer, which will raise an error if it's not a number
            int(x)
            print("Invalid input, enter just letters!!!")  # Error message for invalid input
        except ValueError:
            # If the input can't be converted to an integer, return it as valid input
            return x


def get_valid_num(prompt):
    """
    Asks the user for a number input and ensures the input is either 1 or 2.
    If the user enters an invalid number or a non-numeric value, the function will prompt them again.

    :param prompt: The message to show when asking for input.
    :return: The valid input integer (either 1 or 2).
    """
    while True:
        x = input(prompt)  # Ask for user input
        try:
            # Try converting the input to an integer and check if it's 1 or 2
            if int(x) in [1, 2]:
                return int(x)
            else:
                raise ValueError("Invalid input, choose 1 or 2!!!")  # Raise an error for invalid choices
        except ValueError:
            # Handle the error and show an error message
            print("Invalid input, choose 1 or 2!!!")
