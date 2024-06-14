import random

class SudokuBoardGenerator:

# -----------------------------------------------------------------
    def __init__(self, difficulty=0):
        self.board = [[0]*9 for _ in range(9)]
        if not self.generate_full_board():
            raise ValueError("Failed to generate a valid Sudoku board.")
        self.remove_numbers(difficulty)

# -----------------------------------------------------------------
    def generate_full_board(self):
        """ Fill the board with a complete, valid Sudoku configuration. """
        def fill(position=0):
            if position == 81:
                return True  # The board is completed successfully
            row, col = divmod(position, 9)
            if self.board[row][col] == 0:
                random_numbers = list(range(1, 10))
                random.shuffle(random_numbers)
                for number in random_numbers:
                    if self.valid_placement(row, col, number):
                        self.board[row][col] = number
                        if fill(position + 1):
                            return True
                        self.board[row][col] = 0
            else:
                return fill(position + 1)
            return False

        return fill()

# -----------------------------------------------------------------
    def valid_placement(self, row, col, num):
        """ Check if placing 'num' in (row, col) violates Sudoku rules. """
        block_row, block_col = 3 * (row // 3), 3 * (col // 3)
        if any(self.board[row][i] == num for i in range(9)):
            return False
        if any(self.board[i][col] == num for i in range(9)):
            return False
        if any(self.board[r][c] == num for r in range(block_row, block_row + 3) for c in range(block_col, block_col + 3)):
            return False
        return True

# -----------------------------------------------------------------
    def remove_numbers(self, difficulty):
        """ Remove numbers from the board to set the difficulty. """
        cells_to_keep = 81 - (difficulty * 10)  # Rough formula for difficulty
        cells_to_remove = 81 - cells_to_keep
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1

    def get_board(self):
        return [row[:] for row in self.board]  # Return a copy of the board

# Usage of SudokuBoardGenerator
difficulty = 5  # Adjust difficulty from 0 (easiest) to 9 (hardest)
generator = SudokuBoardGenerator(difficulty)
generated_board = generator.get_board()

# Now, you can pass this board to the SudokuGame class if needed.
