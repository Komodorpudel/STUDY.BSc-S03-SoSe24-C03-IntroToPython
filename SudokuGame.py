from SudokuPauseMenu import SudokuPauseMenu
import os
import datetime
import time

class SudokuGame:
    
# -----------------------------------------------------------------
    def __init__(self, my_main_menu, board = None, user_path=""):
        self.board = board
        self.user_path = user_path
        self.my_main_menu = my_main_menu
        self.my_pause_menu = SudokuPauseMenu(self, self.user_path, my_main_menu)  # Create the pause menu here
        self.mistakes = 0
        self.start_time = time.time()  # Record the start time

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
                self.print_board()
                return False
            if self.board[i][col]['num'] == num:
                print("-------------------------------------")
                print(f"The number {num} is already in this column.")
                self.print_board()
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j]['num'] == num:
                    print("-------------------------------------")
                    print(f"The number {num} is already in this block.")
                    self.print_board()
                    return False
        print(f"Move accepted.")         
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
        elapsed_time = int(time.time() - self.start_time)
        formatted_time = str(datetime.timedelta(seconds=elapsed_time))
        print(f"Mistakes: {self.mistakes} | Time elapsed: {formatted_time}")
        print("- — — — - — — — - — — — -")



# -----------------------------------------------------------------
    def play(self):
        self.print_board()

        while True:
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
                            break
                        print("Try again.")
                    else:
                        print("Move accepted.")
                        self.print_board()
                        if self.check_win():
                            print("!!!YOU WIN!!!")
                            break
                else:
                    print("Please enter a valid row and column between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter integers only.")
            if input("Type 'pause' to go back to pause menu or hit enter to continue: ").lower() == 'pause':
                self.my_pause_menu.display()

# -----------------------------------------------------------------
