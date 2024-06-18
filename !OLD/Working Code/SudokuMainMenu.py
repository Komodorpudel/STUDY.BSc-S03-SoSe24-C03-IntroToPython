import os
import time
from SudokuBoardGenerator import SudokuBoardGenerator
from SudokuSaveLoadManager import SudokuSaveLoadManager
from SudokuGame import SudokuGame
from SudokuHighscoreManager import *
from SudokuAI import *

class SudokuMainMenu:

# -----------------------------------------------------------------
    def __init__(self):
        print( "\n+++++++++++++ WELCOME! +++++++++++++""")
        self.username = input("Enter your Sudoku name: ")
        self.user_path = f"saves/{self.username}"
        self.exit_flag = False
        if not os.path.exists(self.user_path):
            os.makedirs(self.user_path)
            print(f'New user "{self.username}" generated.')
        else:
            print(f'Welcome back "{self.username}"!')


# -----------------------------------------------------------------
    def run_menu(self):
        self.exit_flag = False

        while not self.exit_flag:
            menu_title = f"\n++++++ Main Menu (User: {self.username}) ++++++"
            print(menu_title)
            print("1. Start new game")
            print("2. Start game with AI player")
            print("3. Load unfinished game")
            print("4. Highscore")
            print("5. Exit")

            # Generate a border that matches the length of the menu_title and print it
            border = '+' * len(menu_title.strip())  # Remove the newline for accurate length calculation
            print(border)
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.start_new_game()
            elif choice == '2':
                self.start_new_game_with_ai()
            elif choice == '3':
                self.load_game()
            elif choice == '4':
                self.view_highscore()
            elif choice == '5':
                print("Exiting the game. Goodbye!")
                self.exit_flag = True
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


# -----------------------------------------------------------------
    def start_new_game(self):
        while True:
            try:
                difficulty = int(input("Enter difficulty (0-9): "))
                if 0 <= difficulty <= 9:
                    break
                else:
                    print("Please enter a valid difficulty between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 9.")
        generated_board = SudokuBoardGenerator.generate_board(difficulty)
        my_game = SudokuGame(self, difficulty, generated_board, self.username)
        my_game.play()


# -----------------------------------------------------------------
    def start_new_game_with_ai(self):
        while True:
            try:
                difficulty = int(input("Enter difficulty wih ai should solve (0-9): "))
                if 0 <= difficulty <= 9:
                    break
                else:
                    print("Please enter a valid difficulty between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 9.")
        generated_board = SudokuBoardGenerator.generate_board(difficulty)
        my_game = SudokuGame(self, difficulty, generated_board, self.username)
        my_ai = SudokuAI(my_game)
        my_game.play_with_ai(my_ai)


# -----------------------------------------------------------------
    def load_game(self):
        games = [f for f in os.listdir(self.user_path) if f.endswith('.txt')]
        print(f"DEBUG: Available saved games: {games}")  # Debug print
        if games:
            print("\nAvailable saved games:")
            for i, game in enumerate(games, 1):
                print(f"{i}. {game}")
            game_choice = input("Select a game to load (or type 'back' to return to the main menu): ")
            if game_choice.lower() == 'back':
                return
            else:
                try:
                    selected_game_index = int(game_choice) - 1
                    if 0 <= selected_game_index < len(games):
                        selected_game = games[selected_game_index]
                        print(f"DEBUG: Selected game: {selected_game}")  # Debug print
                        self.load_game_from_file(os.path.join(self.user_path, selected_game))
                    else:
                        print("Invalid selection: Index out of range.")
                except (IndexError, ValueError) as e:
                    print(f"Invalid selection: {e}")
        else:
            print("No saved games available.")


# -----------------------------------------------------------------
    def load_game_from_file(self, game_path):
        board, difficulty, mistakes, elapsed_time = SudokuSaveLoadManager.load_game(game_path)

        # Print out the loaded board for debugging
        """         
        print("DEBUG: Loaded board:")
        for row in board:
            print(' '.join(f"{cell['num']}:{int(cell['mutable'])}" for cell in row))
        """

        my_game = SudokuGame(self, difficulty, board, self.username, mistakes, elapsed_time)
        my_game.mistakes = mistakes
        my_game.play()


# -----------------------------------------------------------------
    def view_highscore(self):
        # Highscore viewing logic
        print("+++++ Highscores +++++")
        SudokuHighscore.display_highscores()
        print("+++ Highscores End +++")

        while True:
            choice = input("Enter 5 to return to main menu: ")
            if choice == '5':
                break

# -----------------------------------------------------------------
if __name__ == "__main__":
    my_main_menu = SudokuMainMenu()
    my_main_menu.run_menu()


# -----------------------------------------------------------------
