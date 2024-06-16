import SudokuUI

class SudokuTUI(SudokuUI):
    def welcome_screen(self):
        print("Welcome to Sudoku!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")  # For simplicity; in practice, handle passwords securely
        return username, password

    def display_main_menu(self):
        print("1. Start New Game")
        print("2. Load Game")
        print("3. View Highscores")
        print("4. Exit")
        return input("Enter your choice: ")

    def display_game_board(self, board):
        for row in board:
            print(' '.join(str(x) for x in row))
        print()

    def get_user_input(self):
        return input("Enter your move (row col num): ")

    def display_message(self, message):
        print(message)

    def display_pause_menu(self):
        print("1. Resume Game")
        print("2. Save Game")
        print("3. Quit to Main Menu")
        return input("Choose an option: ")

    def display_load_menu(self):
        print("Select a saved game to load:")
        # Example: List saved games
        return input("Enter the file name to load: ")

    def display_highscores(self):
        print("Current Highscores:")
        # Example: Fetch and display highscores
