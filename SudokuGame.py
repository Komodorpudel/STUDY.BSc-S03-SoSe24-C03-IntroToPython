class SudokuGame:
# -----------------------------------------------------------------
    def __init__(self, board=None):
        if board is None:
             
            self.board = [
                [5, 3, 4, 6, 7, 8, 9, 1, 0],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ]

            """ 
            self.board = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
            """
        else:
            self.board = board

        self.immutable_numbers = [[not cell == 0 for cell in row] for row in self.board]

# -----------------------------------------------------------------
    def is_valid_move(self, row, col, num):

        if self.immutable_numbers[row][col]:
            print("This cell's value is given and cannot be changed.")
            return False

        for i in range(9):
            if self.board[row][i] == num:
                print(f"The number {num} is already in this row.")
                return False

            if self.board[i][col] == num:
                print(f"The number {num} is already in this column.")
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    print(f"The number {num} is already in this block.")
                    return False

        print(f"Move accepted.")         
        return True


# -----------------------------------------------------------------
    def check_win(self):
        full_set = set(range(1, 10))

        # Check rows and columns
        for i in range(9):
            row_set = set(self.board[i])
            col_set = set(self.board[j][i] for j in range(9))
            if row_set != full_set or col_set != full_set:
                return False

        # Check 3x3 squares
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                square_set = {self.board[r][c] for r in range(x, x+3) for c in range(y, y+3)}
                if square_set != full_set:
                    return False
        return True


# -----------------------------------------------------------------
    def place_number(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
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
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if num == 0:
                    print(". ", end="")
                else:
                    print(f"{num} ", end="")
            print("|")
        print("+ — — — + — — — + — — — +")

# -----------------------------------------------------------------
    def play(self):
        self.print_board()
        while True:
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                num = int(input("Enter number (1-9): "))
                if 0 <= row < 9 and 0 <= col < 9:
                    if not self.place_number(row, col, num):
                        print("Try again.")
                    else:
                        print("Move accepted.")
                        self.print_board() 
                        if self.check_win():
                            print("!!!YOU WIN!!!")
                else:
                    print("Please enter a valid row and column between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter integers only.")
            if input("Type 'exit' to quit or hit enter to continue: ").lower() == 'exit':
                break

# -----------------------------------------------------------------

# To play the game in a terminal
if __name__ == "__main__":
    game = SudokuGame()
    game.play()
