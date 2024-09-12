Google Cybersecurity Certificate Learning Tool
Project Overview
This is a Command Line Interface (CLI) tool designed to help users learn and review terms and definitions from the Google Cybersecurity Certificate. The tool offers two main functionalities:

Searching for terms in the glossary.
Playing a game where definitions are provided, and users guess the correct cybersecurity term.
Release Date: 10.09.2024
Version: 1.0
Created by: Marco Anian

Features
Search Tool: Look up terms and their definitions. If a term is not found, the tool displays the available keywords for further exploration.
Game: A learning game where the tool presents a definition, and the user selects the correct term from multiple choices.
Save Functionality: Users can save their learned terms to a text file for future reference.
How to Use
Search for Terms: You can search for a specific term or browse terms by their first letter.
Option 1: Enter a keyword to search the glossary. If it’s not found, the tool will suggest available terms.
Play the Learning Game: Test your knowledge by guessing the correct term from the definition provided.
Option 2: Play a game where you match definitions with terms.
Exit: You can exit the tool at any time by choosing option 3 in the main menu.

Setup Instructions
Clone the Repository:

bash
Code kopieren
git clone https://github.com/your-username/your-repo-name.git
Install Requirements (if any):

No external dependencies are required for this project.
Run the Program:

bash
Code copy python main.py
Files in the Project
main.py: The main script that runs the program.
error_handlings.py: Contains error-handling functions for input validation.
game.py: Contains the game logic.
main_cli.py: Implements the search tool functionality.
glossary.json: The glossary file containing cybersecurity terms and their definitions.
README.md: This documentation file.
Future Improvements
Add a graphical user interface (GUI) version of the tool.
Implement additional error handling and data validation.
Expand the glossary and game features.
License
This project is open-source and available under the MIT License.