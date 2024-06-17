import SudokuUI
import datetime
from SudokuGame import *

"""
Only handels print and/or returns something.
No game logic checks are done here.
"""

class SudokuUI_Terminal(SudokuUI):

# -----------------------------------------------------------------
    def welcome_screen(self):
        print("Welcome to Sudoku!")
        username = input("Enter your username: ")
        # password = input("Enter your password: ")  # For simplicity; in practice, handle passwords securely
        return username, # password


# -----------------------------------------------------------------
    def display_main_menu(self):
        print("1. Start New Game")
        print("2. Load unfinished Game")
        print("3. View Highscores")
        print("4. Exit")
        return input("Enter your choice: ")
    

# -----------------------------------------------------------------
    def display_board(self, current_game):
        print("+ — — — + — — — + — — — +")
        for i, row in enumerate(current_game.get_board()):
            if i % 3 == 0 and i != 0:
                print("+ — — — + — — — + — — — +")
            print("| ", end="")
            for j, cell in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if cell['num'] == 0:
                    print(". ", end="")
                else:
                    print(f"{cell['num']} ", end="")
            print("|")
        print("+ — — — + — — — + — — — +")
        elapsed_time = current_game.get_total_elapsed_time()
        formatted_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f"Mistakes: {current_game.get_mistakes()} / 3 | Time elapsed: {formatted_time}")
        print("- — — — - — — — - — — — -")

# -----------------------------------------------------------------
    def get_general_input(self, prompt: str) -> str:
        return input(prompt)


# -----------------------------------------------------------------
    def get_next_move(self):
        row, col, num = None, None, None

        row_input = input("Enter row (1-9) or 'pause': ").strip().lower()
        if row_input == 'pause':
            return row_input

        row = int(row_input)
        col = int(input("Enter column (1-9): ").strip())
        num = int(input("Enter number (1-9): ").strip())
        return row, col, num


# -----------------------------------------------------------------
    def display_message(self, message):
        print(message)


# -----------------------------------------------------------------
    def display_pause_menu(self):
        print("1. Resume Game")
        print("2. Save Game")
        print("3. Quit to Main Menu")
        return input("Choose an option: ")


# -----------------------------------------------------------------
    def display_load_menu(self):
        print("Select a saved game to load:")
        # Example: List saved games
        return input("Enter the file name to load: ")


# -----------------------------------------------------------------
    def display_highscores(self):
        print("Current Highscores:")
        # Example: Fetch and display highscores


# -----------------------------------------------------------------
