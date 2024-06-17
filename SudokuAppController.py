import os
import time
from SudokuBoardGenerator import SudokuBoardGenerator
from SudokuSaveLoadManager import SudokuSaveLoadManager
from SudokuGame import SudokuGame
from SudokuHighscore import *
from SudokuAI import *

class SudokuAppController:

# -----------------------------------------------------------------
    def __init__(self, ui):
        # Needs ui, game, and user
        self.ui = ui
        self.game = None  # This will be a GameLogic instance, given when we start game
        self.user = None


# -----------------------------------------------------------------
    def run_welcome_menu(self):
            self.user = self.ui.display_welcome_menu()

            self.user_path = f"saves/{self.user}"
            self.exit_flag = False

            # Create directly if not existing - DIRTY
            if not os.path.exists(self.user_path):
                os.makedirs(self.user_path)
                self.ui.display_message(f'New user "{self.user}" generated.')
                self.run_main_menu()
            else:
                self.ui.display_message(f'Welcome back "{self.user}"!')
                self.run_main_menu()


# -----------------------------------------------------------------
# DONE
    def run_main_menu(self):
        self.exit_flag = False
        while not self.exit_flag:
            choice = self.ui.display_main_menu()

            if choice == '1':
                self.run_new_game_menu()
            elif choice == '2':
                self.run_new_game_with_ai_menu()
            elif choice == '3':
                self.run_load_game_menu()
            elif choice == '4':
                self.run_highscore_menu()
            elif choice == '5':
                self.ui.display_message("Exiting the game. Goodbye!")
                self.exit_flag = True
            else:
                # Not really relevant for GUI since we can limit input options
                self.ui.display_message("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


# -----------------------------------------------------------------
    def run_new_game_menu(self):
        while True:
            try:
                difficulty = int(self.ui.get_general_input("Enter difficulty (0-9): "))
                if 0 <= difficulty <= 9:
                    break
                else:
                    self.ui.display_message("Please enter a valid difficulty between 0 and 9.")
            except ValueError:
                self.ui.display_message("Invalid input. Please enter an integer between 0 and 9.")
        generated_board = SudokuBoardGenerator.generate_board(difficulty)

        #####
            def __init__(self, controller, ui, difficulty, board = None, user = "", mistakes=0, total_elapsed_time=0):
        self.game = SudokuGame(self, self.ui, difficulty, generated_board, self.user)
        self.game.play()

# -----------------------------------------------------------------
def run_pause_menu(self):
    while True:
        print("\n++++++ Pause Menu ++++++")
        print("1. Resume game")
        print("2. Save game")
        print("3. Return to main menu")
        print("+++++++++++++++++++++++")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nResuming game...")
            self.game.play()
            break
        elif choice == '2':
            SudokuSaveLoadManager.save_game(self.game)
            print("Game saved.")
        elif choice == '3':
            print("\nReturning to main menu...")
            self.game.get_main_menu().run_menu()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")




# -----------------------------------------------------------------
    def run_new_game_with_ai_menu(self):
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
        my_game = SudokuGame(self, difficulty, generated_board, self.user)
        my_ai = SudokuAI(my_game)
        my_game.play_with_ai(my_ai)


# -----------------------------------------------------------------
    def run_load_game_menu(self):
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

        my_game = SudokuGame(self, difficulty, board, self.user, mistakes, elapsed_time)
        my_game.mistakes = mistakes
        my_game.play()


# -----------------------------------------------------------------
    def run_highscore_menu(self):
        # Highscore viewing logic
        print("+++++ Highscores +++++")
        SudokuHighscore.display_highscores()
        print("+++ Highscores End +++")
        
        while True:
            choice = input("Enter 5 to return to main menu: ")
            if choice == '5':
                break

