import os
import datetime
# from SudokuGame import SudokuGame

class SudokuPauseMenu:
    def __init__(self, game, user_path, main_menu):
        self.game = game
        self.user_path = user_path
        self.main_menu = main_menu

    def display(self):
        while True:
            print("\n++++++ Pause Menu ++++++")
            print("1. Resume game")
            print("2. Save game")
            print("3. Return to main menu")
            choice = input("Enter your choice (1-3): ")
            if choice == '1':
                print("Resuming game...")
                self.game.print_board()

                break
            elif choice == '2':
                self.save_game()
            elif choice == '3':
                print("Returning to main menu...")
                self.main_menu.display_menu()
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def save_game(self):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        game_name = f"{self.game.user_path}_{timestamp}.txt"
        save_path = os.path.join(self.user_path, game_name)
        with open(save_path, 'w') as f:
            for row in self.game.board:
                f.write(' '.join(f"{cell['num']}:{int(cell['mutable'])}" for cell in row) + '\n')
        print(f"Game saved as {game_name}.")