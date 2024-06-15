from SudokuPauseMenu import SudokuPauseMenu
import datetime
from SudokuStopwatch import SudokuStopwatch
from SudokuHighscore import *

class SudokuGame:

# -----------------------------------------------------------------
    def __init__(self, my_main_menu, difficulty, board = None, username = "", mistakes=0, total_elapsed_time=0):
        self.board = board
        self.username = username
        self.my_main_menu = my_main_menu
        self.difficulty = difficulty
        self.my_pause_menu = SudokuPauseMenu(self)  # Create the pause menu here
        self.mistakes = mistakes
        self.previous_elapsed_time = total_elapsed_time
        self.my_stopwatch = SudokuStopwatch()
        self.is_paused = False

        if board is None:
            self.board = [
                [{'num': 0, 'mutable': True}, {'num': 0, 'mutable': True}, {'num': 4, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 2, 'mutable': False}],
                [{'num': 6, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 3, 'mutable': False}, {'num': 4, 'mutable': False}, {'num': 8, 'mutable': False}],
                [{'num': 1, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 3, 'mutable': False}, {'num': 4, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 7, 'mutable': False}],
                [{'num': 8, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 4, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 3, 'mutable': False}],
                [{'num': 4, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 3, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 1, 'mutable': False}],
                [{'num': 7, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 3, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 4, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 6, 'mutable': False}],
                [{'num': 9, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 3, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 4, 'mutable': False}],
                [{'num': 2, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 4, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 9, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 3, 'mutable': False}, {'num': 5, 'mutable': False}],
                [{'num': 3, 'mutable': False}, {'num': 4, 'mutable': False}, {'num': 5, 'mutable': False}, {'num': 2, 'mutable': False}, {'num': 8, 'mutable': False}, {'num': 6, 'mutable': False}, {'num': 1, 'mutable': False}, {'num': 7, 'mutable': False}, {'num': 9, 'mutable': False}]
            ]

        else:
            self.board = board

    # Getter functions
    def get_difficulty(self):
        return self.difficulty

    def get_board(self):
        return self.board

    def get_total_elapsed_time(self):
        return self.previous_elapsed_time + self.my_stopwatch.get_elapsed_time()

    def get_username(self):
        return self.username

    def get_main_menu(self):
        return self.my_main_menu


# -----------------------------------------------------------------
    def is_valid_move(self, row, col, num):

        if not self.board[row][col]['mutable']:
            print("-------------------------------------")
            print("This cell's value is given and cannot be changed.")
            self.print_board()
            return False

        for i in range(9):
            if self.board[row][i]['num'] == num:
                print("-------------------------------------")
                print(f"The number {num} is already in this row.")
                self.mistakes += 1
                self.print_board()
                return False
            if self.board[i][col]['num'] == num:
                print("-------------------------------------")
                print(f"The number {num} is already in this column.")
                self.mistakes += 1
                self.print_board()
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j]['num'] == num:
                    print("-------------------------------------")
                    print(f"The number {num} is already in this block.")
                    self.mistakes += 1
                    self.print_board()
                    return False
        print("Move accepted.")
        return True


# -----------------------------------------------------------------
    def check_win(self):
        full_set = set(range(1, 10))

        # Check rows and columns
        for i in range(9):
            row_set = set(cell['num'] for cell in self.board[i])
            col_set = set(self.board[j][i]['num'] for j in range(9))
            if row_set != full_set or col_set != full_set:
                return False

        # Check 3x3 squares
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                square_set = {self.board[r][c]['num'] for r in range(x, x+3) for c in range(y, y+3)}
                if square_set != full_set:
                    return False
        return True


# -----------------------------------------------------------------
    def place_number(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.board[row][col]['num'] = num
            return True
        return False


# -----------------------------------------------------------------
# SAH: Complete

    """
    def print_board(self):
        print("+ — — — + — — — + — — — +")
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("+ — — — + — — — + — — — +")
            print("| ", end="")
            for j, cell in enumerate(row):
                print(f"DEBUG: cell = {cell}")  # Debug print to check cell type
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if isinstance(cell, dict) and cell['num'] == 0:
                    print(". ", end="")
                elif isinstance(cell, dict):
                    print(f"{cell['num']} ", end="")
                else:
                    print("Error: cell is not a dictionary")
            print("|")
        print("+ — — — + — — — + — — — +")
        elapsed_time = int(self.previous_elapsed_time + self.my_stopwatch.get_elapsed_time())
        formatted_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f"Mistakes: {self.mistakes} | Time elapsed: {formatted_time}")
        print("- — — — - — — — - — — — -")
    """

    def print_board(self):
        print("+ — — — + — — — + — — — +")
        for i, row in enumerate(self.board):
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
        elapsed_time = self.previous_elapsed_time + self.my_stopwatch.get_elapsed_time()
        formatted_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f"Mistakes: {self.mistakes} / 3 | Time elapsed: {formatted_time}")
        print("- — — — - — — — - — — — -")


# -----------------------------------------------------------------
    def play(self):
        self.print_board()
        self.my_stopwatch.start() # We start counting

        while not self.is_paused:
            try:
                row_input = input("Enter row (1-9) or 'pause': ").strip().lower()
                if row_input == 'pause':
                    self.my_pause_menu.display()
                    continue
                row = int(row_input)
                col = int(input("Enter column (1-9): ").strip())
                num = int(input("Enter number (1-9): ").strip())

                row, col = row - 1, col - 1
                if 0 <= row < 9 and 0 <= col < 9:
                    if not self.place_number(row, col, num):
                        if self.mistakes >= 3:
                            print("!!!YOU LOSE!!!")
                            print(f"Score substracted: {self.difficulty * -1}")
                            SudokuHighscore.set_highscore(self.username, self.difficulty * -1)
                            highscore = SudokuHighscore.get_user_highscore(self.username)
                            print(f"New total score: {highscore}")
                            self.my_stopwatch.pause()
                            break
                        print("Try again.")
                    else:
                        print("Move accepted.")
                        self.print_board()
                        if self.check_win():
                            print("!!!YOU WIN!!!")
                            print(f"Score added: {self.difficulty}")
                            SudokuHighscore.set_highscore(self.username, self.difficulty)
                            highscore = SudokuHighscore.get_user_highscore(self.username)
                            print(f"New total score: {highscore}")
                            self.my_stopwatch.pause()
                            break

                else:
                    print("Please enter a valid row and column between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter integers only.")
            if input("Type 'pause' to go back to pause menu or hit enter to continue: ").lower() == 'pause':
                self.is_paused = True
                self.my_stopwatch.pause()
                self.my_pause_menu.display()


# -----------------------------------------------------------------
