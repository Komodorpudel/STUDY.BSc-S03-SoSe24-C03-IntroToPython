from SudokuSaveLoadManager import *

class SudokuPauseMenu:
    def __init__(self, game, username, main_menu):
        self.game = game
        self.username = username
        self.main_menu = main_menu
        self.save_load_manager = SudokuSaveLoadManager(username)

    def display(self):
        while True:
            print("\n++++++ Pause Menu ++++++")
            print("1. Resume game")
            print("2. Save game")
            print("3. Return to main menu")
            print("\n++++++++++++++++++++")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                print("\nResuming game...")
                self.game.print_board()
                break
            elif choice == '2':
                self.save_load_manager.save_game(self.game)
                print("Game saved.")
            elif choice == '3':
                print("\nReturning to main menu...")
                self.game.is_paused = True  # Set the game's pause flag
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
