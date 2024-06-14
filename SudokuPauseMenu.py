import os
import datetime
import time
# from SudokuGame import SudokuGame

class SudokuPauseMenu:
    def __init__(self, game, username, main_menu):
        self.game = game
        self.username = username
        self.main_menu = main_menu

    def display(self):
        while True:
            print("\n++++++ Pause Menu ++++++")
            print("1. Resume game")
            print("2. Save game")
            print("3. Return to main menu")
            print("\n++++++++++++++++++++")
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                print("\nResuming game...")
                self.game.play()
                self.game.print_board()

                break
            elif choice == '2':
                self.save_game()
            elif choice == '3':
                print("\nReturning to main menu...")
                self.game.is_paused = True 
                self.main_menu.display_menu()
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def save_game(self):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        game_name = f"{self.username}_{timestamp}.txt"
        save_path = os.path.join("saves", self.username, game_name)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'w') as f:
            for row in self.game.board:
                f.write(' '.join(f"{cell['num']}:{int(cell['mutable'])}" for cell in row) + '\n')
            f.write(f"Mistakes: {self.game.mistakes}\n")
            elapsed_time = int(time.time() - self.game.start_time)
            formatted_time = str(datetime.timedelta(seconds=elapsed_time))
            f.write(f"Time elapsed: {formatted_time}\n")
        print(f"Game saved as {game_name}.")

