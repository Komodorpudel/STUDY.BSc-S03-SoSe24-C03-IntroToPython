import subprocess
import time

class SudokuAI:
    def __init__(self, game):
        self.game = game
        
    def make_move(self):
        # Logic to determine the best move
        # For simplicity, we're just choosing a random move that's valid
        for row in range(9):
            for col in range(9):
                if self.game.is_valid_move(row, col, 1):  # Checking for a valid move
                    self.game.place_number(row, col, 1)
                    return True
        return False

# Usage
game = SudokuGame()  # Assuming this is your game class
ai = SudokuAI(game)
while not game.check_win():
    ai.make_move()
    game.print_board()

def simulate_ai_interaction():
    # Start the game process
    process = subprocess.Popen(['python', 'sudoku_game.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        if "Enter row" in output:
            # Simulate entering a valid row number
            process.stdin.write('1\n')
            process.stdin.flush()
        elif "Enter column" in output:
            # Simulate entering a valid column number
            process.stdin.write('1\n')
            process.stdin.flush()
        elif "Enter number" in output:
            # Simulate entering a valid number
            process.stdin.write('5\n')
            process.stdin.flush()
        elif "YOU WIN" in output or "YOU LOSE" in output:
            break
        time.sleep(1)  # Slow down the loop for demonstration purposes

simulate_ai_interaction()
