from SudokuStopwatch import SudokuStopwatch
from SudokuHighscore import *

class SudokuGame:

# -----------------------------------------------------------------
    def __init__(self, controller, difficulty, board = None, user = "", mistakes=0, total_elapsed_time=0):
        self.controller = controller
        self.ui = controller.get_ui()
        self.ui.set_game(self)
        
        self.difficulty = difficulty
        self.board = board
        self.user = user
        self.mistakes = mistakes
        self.previous_elapsed_time = total_elapsed_time

        self.my_stopwatch = SudokuStopwatch()
        self.is_paused = False
        self.my_stopwatch.start() # We start counting



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
    
    def get_mistakes(self):
        return self.mistakes

    def get_total_elapsed_time(self):
        return self.previous_elapsed_time + self.my_stopwatch.get_elapsed_time()

    def get_user(self):
        return self.user

# -----------------------------------------------------------------
# DONE
    def is_valid_move(self, row, col, num):

        if not self.board[row][col]['mutable']:
            self.ui.display_message("This cell's value is given and cannot be changed.")
            self.ui.display_board()
            return False

        for i in range(9):
            if self.board[row][i]['num'] == num:
                self.ui.display_message(f"The number {num} is already in this row.")
                self.mistakes += 1
                self.ui.display_board()
                return False
            if self.board[i][col]['num'] == num:
                self.ui.display_message(f"The number {num} is already in this column.")
                self.mistakes += 1
                self.ui.display_board()
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j]['num'] == num:
                    self.ui.display_message(f"The number {num} is already in this block.")
                    self.mistakes += 1
                    self.ui.display_board()
                    return False
        self.ui.display_message("Move accepted.")
        return True


# -----------------------------------------------------------------
# DONE
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
    def play(self):
        self.ui.display_board()

        while True:
            try:
                row, col, num = self.ui.get_next_move()
                if row == 'pause':
                    self.is_paused = True
                    self.controller.run_pause_menu()
                    break

                row, col = row - 1, col - 1
                if 0 <= row < 9 and 0 <= col < 9:
                    if not self.place_number(row, col, num):
                        if self.mistakes >= 3:
                            self.ui.display_message("!!!YOU LOSE!!!")
                            self.my_stopwatch.pause()
                            self.ui.display_message(f"Score substracted: {self.difficulty * -1}")
                            SudokuHighscore.set_highscore(self.user, self.difficulty * -1)
                            highscore = SudokuHighscore.get_user_highscore(self.user)
                            self.ui.display_message(f"New total score: {highscore}")
                            break

                        self.ui.display_message("Try again.")
                    else:
                        self.ui.display_board()
                        if self.check_win():
                            self.ui.display_message("!!!YOU WIN!!!")
                            self.my_stopwatch.pause()
                            self.ui.display_message(f"Score added: {self.difficulty}")
                            SudokuHighscore.set_highscore(self.user, self.difficulty)
                            highscore = SudokuHighscore.get_user_highscore(self.user)
                            self.ui.display_message(f"New total score: {highscore}")
                            break

                else:
                    self.ui.display_message("Please enter a valid row and column between 1 and 9.")
            except ValueError:
                self.ui.display_message("Invalid input. Please enter integers only.")

            if self.ui.get_general_input("Type 'pause' to open pause menu or hit enter to continue: ").lower() == 'pause':
                self.my_stopwatch.pause()
                self.controller.run_pause_menu()
                break


# -----------------------------------------------------------------
# DONE
    def play_with_ai(self, ai_player):
        """Run the game with AI making moves."""
        self.ui.display_board()
        while not self.check_win():
            move = ai_player.decide_move()
            if move:
                row, col, num = move
                if self.is_valid_move(row, col, num):
                    self.place_number(row, col, num)
                    self.ui.display_message(f"AI placed {num} at ({row+1}, {col+1})")
                    self.ui.display_board()
                if self.check_win():
                    self.ui.display_message("AI wins!")
                    break
            else:
                self.ui.display_message("AI could not make a valid move.")
                break


# -----------------------------------------------------------------
         