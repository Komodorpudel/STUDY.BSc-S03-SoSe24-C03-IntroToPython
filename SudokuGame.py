class SudokuGame:
    def __init__(self, board=None):
        if board is None:
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
        else:
            self.board = board

# -----------------------------------------------------------------
    def is_valid_move(self, row, col, num):
        if self.board[row][col] != 0:
            return False
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
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
        print("— — — — — — — — — — — — —")
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print("— — — — — — — — — — — — —")
            print("| ", end="")
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if num == 0:
                    print(". ", end="")
                else:
                    print(f"{num} ", end="")
            print("|")
        print("— — — — — — — — — — — —")

# -----------------------------------------------------------------
    def play(self):
        self.print_board()
        while True:
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                num = int(input("Enter number (1-9): "))
                if 0 <= row < 9 and 0 <= col < 9:
                    if self.place_number(row, col, num):
                        print("Move accepted.")
                        self.print_board()
                    else:
                        print("Invalid move.")
                else:
                    print("Please enter a valid row and column between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter integers only.")
            if input("Type 'exit' to quit or hit enter to continue: ").lower() == 'exit':
                break

# To play the game in a terminal
if __name__ == "__main__":
    game = SudokuGame()
    game.play()
