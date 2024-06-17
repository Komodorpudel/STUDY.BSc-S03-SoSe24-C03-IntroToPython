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
        self.menu_width = 0
        self.border = None


# -----------------------------------------------------------------
    def display_welcome_menu(self):
        print( "\n+++++++++++++ WELCOME! +++++++++++++""")
        self.user = input("Enter your Sudoku name: ")
        # password = input("Enter your password: ")  # For simplicity; in practice, handle passwords securely
        return self.user #, password # password


# -----------------------------------------------------------------
    def display_main_menu(self):
        menu_title = f"\n++++++++++ Main Menu (User: {self.user}) +++++++++++"
        self.menu_width = len(menu_title.strip())
        self.border = '+' * self.menu_width # Remove the newline for accurate length calculation
        print(menu_title)
        print("1. Start new game")
        print("2. Start game with AI player")
        print("3. Load unfinished game")
        print("4. Highscore")
        print("5. Exit")

        print(self.border)
        return input("Enter your choice (1-5): ")


# -----------------------------------------------------------------
    def display_board(self):
        print(self.border)
        print(f"{self.user}'s current game | Difficulty: {self.game.get_difficulty()} / 9")
        print("+ — — — + — — — + — — — +")
        for i, row in enumerate(self.game.get_board()):
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
        elapsed_time = self.game.get_total_elapsed_time()
        formatted_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f"Mistakes: {self.game.get_mistakes()} / 3 | Time elapsed: {formatted_time}")
        print(self.border)


# -----------------------------------------------------------------
    def display_pause_menu(self):
        print(self.border)
        print("1. Resume game")
        print("2. Save game")
        print("3. Return to main menu")
        print(self.border)
        return input("Enter your choice (1-3): ")


# -----------------------------------------------------------------
    def display_load_menu(self):
        print("Select a saved game to load:")
        # Example: List saved games
        return input("Enter the file name to load: ")


# -----------------------------------------------------------------
    def display_highscore_menu(self):
        highscores = SudokuHighscore.get_highscores()
        title = " Highscores "
        print("\n" + title.center(self.menu_width, '+'))
        for user, score in highscores:
            print(f"{user}: {score}")
        print(self.border)
        # Example: Fetch and display highscores

# -----------------------------------------------------------------
    def get_general_input(self, prompt: str) -> str:
        return input(prompt)


# -----------------------------------------------------------------
    def get_next_move(self):
        #### ISSUE HERE when pause is returned
        row, col, num = None, 1, 1

        row = input("Enter row (1-9) or 'pause': ").strip().lower()
        if row == 'pause':
            return row

        row = int(row)
        col = int(input("Enter column (1-9): ").strip())
        num = int(input("Enter number (1-9): ").strip())
        return row, col, num


# -----------------------------------------------------------------
    def display_message(self, message):
        print(message)





# -----------------------------------------------------------------
