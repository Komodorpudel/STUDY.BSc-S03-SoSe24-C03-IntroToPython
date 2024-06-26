import os
import sys
from SudokuBoardGenerator import SudokuBoardGenerator
from SudokuSaveLoadManager import SudokuSaveLoadManager
from SudokuGame import SudokuGame
from SudokuHighscoreManager import SudokuHighscoreManager
from SudokuAI import *

class SudokuAppController:

# -----------------------------------------------------------------
    def __init__(self, ui):
        # Needs ui, game, and user
        self.ui = ui
        self.game = None  # This will be a GameLogic instance, given by game when we start game
        self.user = None
        self.user_save_path = None


# -----------------------------------------------------------------
    def get_ui(self):
        return self.ui


# -----------------------------------------------------------------
    def get_user(self):
        return self.user


# -----------------------------------------------------------------
    def run_welcome_menu(self):
        self.user = self.ui.display_welcome_menu()
        
        # Create directly if not existing
        if not os.path.exists(SudokuSaveLoadManager.get_user_path(self.user)):
            self.user_save_path = SudokuSaveLoadManager.set_user_path(self.user)
            self.ui.display_message(f'New user "{self.user}" generated.')
        else:
            self.user_save_path = SudokuSaveLoadManager.get_user_path(self.user)
            self.ui.display_message(f'Welcome back "{self.user}"!')
 
        self.run_main_menu()


# -----------------------------------------------------------------
    def run_main_menu(self):
        while True:
            choice = self.ui.display_main_menu()

            if choice == '1':
                self.run_new_game_menu()
                break
            elif choice == '2':
                self.run_new_game_with_ai_menu()
                break
            elif choice == '3':
                self.run_load_game_menu()
                break
            elif choice == '4':
                self.run_highscore_menu()
                break
            elif choice == '5':
                self.ui.display_message("Exiting the game. Goodbye!")
                sys.exit(0)
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
        # generated_board = SudokuBoardGenerator.generate_board(difficulty)
        generated_board = None

        #####
        self.game = SudokuGame(self, difficulty, generated_board, self.user)
        self.game.play()


# -----------------------------------------------------------------
    def run_pause_menu(self):
        while True:
            choice = self.ui.display_pause_menu()
            if choice == '1':
                self.ui.display_message("Resuming game...")
                self.game.play()
                break

            elif choice == '2':
                ####################
                game_name = SudokuSaveLoadManager.save_game(self.game)
                self.get_ui().display_message(f"Game saved as {game_name}.")

            elif choice == '3':
                self.ui.display_message("Returning to main menu...")
                self.run_main_menu()
                break

            else:
                self.ui.display_message("Invalid choice. Please enter 1, 2, or 3.")


# -----------------------------------------------------------------
    def run_new_game_with_ai_menu(self):
        while True:
            try:
                difficulty = int(self.ui.get_general_input("Enter difficulty of board that ai should solve (0-9): "))
                if 0 <= difficulty <= 9:
                    break
                else:
                    self.ui.display_message("Please enter a valid difficulty between 0 and 9.")
            except ValueError:
                self.ui.display_message("Invalid input. Please enter an integer between 0 and 9.")
        generated_board = SudokuBoardGenerator.generate_board(difficulty)
        my_game = SudokuGame(self, difficulty, generated_board, self.user)
        my_ai = SudokuAI(my_game)
        my_game.play_with_ai(my_ai)


# -----------------------------------------------------------------
    def run_load_game_menu(self):
        # print(f"DEBUG: Available saved games: {games}")  # Debug print

        game_choice = self.ui.display_load_menu()
        if game_choice.lower() == 'back':
            self.run_main_menu()
        else:
            game_path = os.path.join(self.user_save_path, game_choice)
            self.game = SudokuSaveLoadManager.load_game(game_path, self)
            self.game.play()


# -----------------------------------------------------------------
    def run_highscore_menu(self):
        # Highscore viewing logic
        self.ui.display_highscore_menu()

        while True:
            choice = self.ui.get_general_input("Enter 5 to return to main menu: ")
            if choice == '5':
                self.run_main_menu()


# -----------------------------------------------------------------
