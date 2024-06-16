import time

class SudokuAI:

# -----------------------------------------------------------------
    def __init__(self, game):
        self.game = game
        self.board = None


# -----------------------------------------------------------------
    def decide_move(self):
        # Analyze the board and return the next move as (row, col, num)
        self.board = self.game.get_board()
        time.sleep(2)  # Simulate think time

        for row in range(9):
            for col in range(9):
                if self.board[row][col]['num'] == 0:  # Find the first empty spot
                    for num in range(1, 10):  # Try numbers 1-9
                        if self.valid_move(row, col, num):
                            return (row, col, num)
        return None


# -----------------------------------------------------------------
    def valid_move(self, row, col, num):
        if not self.board[row][col]['mutable']:
            return False
        for i in range(9):
            if self.board[row][i]['num'] == num:
                # print(f"The number {num} is already in this row.")
                return False
            if self.board[i][col]['num'] == num:
                # print(f"The number {num} is already in this column.")
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j]['num'] == num:
                    # print(f"The number {num} is already in this block.")
                    return False
        return True


# -----------------------------------------------------------------
