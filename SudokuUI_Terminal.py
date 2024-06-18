import datetime
from SudokuUI import SudokuUI
from SudokuGame import *
from SudokuSaveLoadManager import *

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
    def set_game(self, game):
        self.game = game


# -----------------------------------------------------------------
    def display_welcome_menu(self):
        welcome = "++++++++++++++++++ WELCOME! ++++++++++++++++++"
        print(welcome)
        self.menu_width = len(welcome.strip())
        self.user = input("Enter your Sudoku name: ")
        # password = input("Enter your password: ")  # For simplicity; in practice, handle passwords securely
        
        return self.user #, password # password


# -----------------------------------------------------------------
    def display_main_menu(self):
        menu_title = f"\n++++++++++ Main Menu (User: {self.user}) +++++++++++"
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
        title = " Saved games: "
        print("\n" + title.center(self.menu_width, '+'))

        saved_games = SudokuSaveLoadManager.get_list_of_saved_games(self.user)

        if saved_games:
            for i, game in enumerate(saved_games, 1):
                print(f"{i}. {game}")
            selected_game_index = input("Select a game to load (or type 'return' to return to the main menu): ")
        else:
            print("No saved games available.")
            print(self.border)

        try:
            selected_game_index = int(selected_game_index) - 1
            if 0 <= selected_game_index < len(saved_games):
                selected_game = saved_games[selected_game_index]
                # print(f"DEBUG: Selected game: {selected_game}")  # Debug print

            else:
                self.display_message("Invalid selection: Index out of range.")
        except (IndexError, ValueError) as e:
            self.display_message(f"Invalid selection: {e}")

        return selected_game


# -----------------------------------------------------------------
    def display_highscore_menu(self):
        highscores = SudokuHighscoreManager.get_highscores()
        title = " Highscores: "
        print("\n" + title.center(self.menu_width, '+'))
        for user, score in highscores:
            print(f"{user}: {score}")
        print(self.border)


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
