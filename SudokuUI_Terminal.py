from SudokuUI import SudokuUI
import datetime
from SudokuGame import *

"""
Only handels print and/or returns something.
No game logic checks are done here.
"""

class SudokuUI_Terminal(SudokuUI):

# -----------------------------------------------------------------
    def __init__(self, game=None, user=None):
        self.game = game
        self.user = user


# -----------------------------------------------------------------
    def display_welcome_menu(self):
        print( "\n+++++++++++++ WELCOME! +++++++++++++""")
        self.user = input("Enter your Sudoku name: ")
        # password = input("Enter your password: ")  # For simplicity; in practice, handle passwords securely
        return self.user #, password # password


# -----------------------------------------------------------------
    def display_main_menu(self):
        menu_title = f"\n++++++ Main Menu (User: {self.user}) ++++++"
        print(menu_title)
        print("1. Start new game")
        print("2. Start game with AI player")
        print("3. Load unfinished game")
        print("4. Highscore")
        print("5. Exit")

        # Generate a border that matches the length of the menu_title and print it
        border = '+' * len(menu_title.strip())  # Remove the newline for accurate length calculation
        print(border)
        return input("Enter your choice (1-5): ")
    

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
    def display_pause_menu(self):
        print("\n++++++ Pause Menu ++++++")
        print("1. Resume game")
        print("2. Save game")
        print("3. Return to main menu")
        print("+++++++++++++++++++++++")
        return input("Enter your choice (1-3): ")


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
