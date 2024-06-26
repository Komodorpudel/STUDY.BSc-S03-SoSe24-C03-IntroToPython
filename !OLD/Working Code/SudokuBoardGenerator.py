import random

class SudokuBoardGenerator:

# -----------------------------------------------------------------
    def __init__(self, difficulty=0):
        self.board = [[{'num': 0, 'mutable': True} for _ in range(9)] for _ in range(9)]
        if not self.generate_full_board():
            raise ValueError("Failed to generate a valid Sudoku board.")
        self.remove_numbers(difficulty)


# -----------------------------------------------------------------
    def generate_full_board(self):
        def fill(position=0):
            if position == 81:
                return True
            row, col = divmod(position, 9)
            if self.board[row][col]['num'] == 0:
                random_numbers = list(range(1, 10))
                random.shuffle(random_numbers)
                for number in random_numbers:
                    if self.valid_placement(row, col, number):
                        self.board[row][col]['num'] = number
                        if fill(position + 1):
                            return True
                        self.board[row][col]['num'] = 0
            else:
                return fill(position + 1)
            return False
        return fill()


# -----------------------------------------------------------------
    def valid_placement(self, row, col, num):
        block_row, block_col = 3 * (row // 3), 3 * (col // 3)
        if any(self.board[row][i]['num'] == num for i in range(9)):
            return False
        if any(self.board[i][col]['num'] == num for i in range(9)):
            return False
        if any(self.board[r][c]['num'] == num for r in range(block_row, block_row + 3) for c in range(block_col, block_col + 3)):
            return False
        return True


# -----------------------------------------------------------------
    def remove_numbers(self, difficulty):
        cells_to_keep = 81 - (difficulty * 10)
        cells_to_remove = 81 - cells_to_keep
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col]['num'] != 0:
                self.board[row][col] = {'num': 0, 'mutable': True}
                cells_to_remove -= 1
        # Set immutability for the remaining cells
        for row in self.board:
            for cell in row:
                if cell['num'] != 0:
                    cell['mutable'] = False


# -----------------------------------------------------------------
    def get_board(self):
        return [[cell.copy() for cell in row] for row in self.board]


# -----------------------------------------------------------------
    @classmethod
    def generate_board(cls, difficulty=0):
        generator = cls(difficulty)
        return generator.get_board()


# -----------------------------------------------------------------
