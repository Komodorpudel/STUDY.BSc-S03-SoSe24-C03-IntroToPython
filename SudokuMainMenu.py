import os
from SudokuBoardGenerator import SudokuBoardGenerator
from SudokuGame import SudokuGame
import time

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
    def display_menu(self):
        while not self.exit_flag:
            menu_title = f"\n++++++ Main Menu (User: {self.username}) ++++++"
            print(menu_title)
            print("1. Start new game")
            print("2. Load unfinished game")
            print("3. Highscore")
            print("4. Exit")

            # Generate a border that matches the length of the menu_title and print it
            border = '+' * len(menu_title.strip())  # Remove the newline for accurate length calculation
            print(border)
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.start_new_game()
            elif choice == '2':
                self.load_game()
            elif choice == '3':
                self.view_highscore()
            elif choice == '4':
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
    def load_game(self):
        games = [f for f in os.listdir(self.user_path) if f.endswith('.txt')]
        if games:
            print("\nAvailable saved games:")
            for i, game in enumerate(games, 1):
                print(f"{i}. {game}")
            game_choice = input("Select a game to load (or type 'back' to return to the main menu): ")
            if game_choice.lower() == 'back':
                return
            else:
                try:
                    selected_game = games[int(game_choice) - 1]
                    self.load_game_from_file(os.path.join(self.user_path, selected_game))
                except (IndexError, ValueError):
                    print("Invalid selection.")
        else:
            print("No saved games available.")

# -----------------------------------------------------------------
    def load_game_from_file(self, game_path):
        print(f"Loading game from {game_path}")
        with open(game_path, 'r') as f:
            board = []
            mistakes = 0
            elapsed_time = 0
            for line in f:
                if line.startswith("Mistakes:"):
                    mistakes = int(line.split(": ")[1])
                elif line.startswith("Time elapsed:"):
                    elapsed_time_str = line.split(": ")[1].strip()
                    time_parts = elapsed_time_str.split(':')
                    elapsed_time = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
                else:
                    row = []
                    cells = line.strip().split()
                    for cell in cells:
                        num, mutable = cell.split(':')
                        row.append({'num': int(num), 'mutable': bool(int(mutable))})
                    board.append(row)
        
        print("Loaded board:")
        for row in board:
            print(' '.join(f"{cell['num']}:{int(cell['mutable'])}" for cell in row))

        my_game = SudokuGame(self, board, self.username)
        my_game.mistakes = mistakes
        my_game.start_time = time.time() - elapsed_time
        my_game.play()

# -----------------------------------------------------------------
    def play_game(self, game_path):
        print(f"Loading game from {game_path}")
        # Here you would actually load the game state and continue the game


# -----------------------------------------------------------------

    def view_highscore(self):
        # Highscore viewing logic
        print("+++++ Highscores +++++")
        # Here you would fetch and display high scores from a file or database

# -----------------------------------------------------------------
if __name__ == "__main__":
    my_main_menu = SudokuMainMenu()
    my_main_menu.display_menu()
