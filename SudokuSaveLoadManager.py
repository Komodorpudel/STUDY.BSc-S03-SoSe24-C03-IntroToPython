import os
import datetime
from SudokuAppController import *
from SudokuGame import SudokuGame

class SudokuSaveLoadManager:

    def __init__(self, controller):
        self.controller = controller
        self.user = controller.get_user()

# -----------------------------------------------------------------

    def init_user_path(self):
        user_path = f"saves/{user}"
        os.makedirs(user_path, exist_ok=True)
        return user_path

# -----------------------------------------------------------------

    def save_game(self, game):
        user_path = self.init_user_path(game.get_username())
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        game_name = f"{game.get_username()}_{timestamp}.txt"
        save_path = os.path.join(user_path, game_name)
        with open(save_path, 'w') as f:
            f.write(f"Difficulty: {game.get_difficulty()}\n")
            for row in game.get_board():
                f.write(' '.join(f"{cell['num']}:{int(cell['mutable'])}" for cell in row) + '\n')
            f.write(f"Mistakes: {game.mistakes}\n")
            elapsed_time = game.get_total_elapsed_time()
            f.write(f"Elapsed time: {elapsed_time}\n")
        print(f"Game saved as {game_name}.")


# -----------------------------------------------------------------

    def load_game(self, game_path):
        print(f"Loading game from {game_path}")
        with open(game_path, 'r') as f:
            board = []
            mistakes = 0
            elapsed_time = 0
            difficulty = 0  # Default difficulty
            for line in f:
                if line.startswith("Difficulty:"):
                    difficulty = int(line.split(": ")[1])
                elif line.startswith("Mistakes:"):
                    mistakes = int(line.split(": ")[1])
                elif line.startswith("Elapsed time:"):
                    try:
                        elapsed_time = int(line.split(": ")[1])
                    except ValueError as e:
                        print(f"Error parsing elapsed time: {e}")
                        continue
                else:
                    row = []
                    cells = line.strip().split()
                    for cell in cells:
                        if ':' in cell:
                            num, mutable = cell.split(':')
                            row.append({'num': int(num), 'mutable': bool(int(mutable))})
                    if row:
                        board.append(row)

        # Print out the loaded board for debugging
        """
        print("DEBUG: Loaded board:")
        for row in board:
            print(' '.join(f"{cell['num']}:{int(cell['mutable'])}" for cell in row))
        """
    loaded_game = SudokuGame()

    def __init__(self, controller, difficulty, board = None, user = "", mistakes=0, total_elapsed_time=0):
        return board, difficulty, mistakes, elapsed_time


# -----------------------------------------------------------------
