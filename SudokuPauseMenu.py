class PauseMenu:
    def __init__(self, game, user_path):
        self.game = game
        self.user_path = user_path

    def display(self):
        while True:
            print("\n++++++ Pause Menu ++++++")
            print("1. Resume game")
            print("2. Save game")
            print("3. Return to main menu")
            choice = input("Enter your choice (1-3): ")
            if choice == '1':
                print("Resuming game...")
                break
            elif choice == '2':
                self.save_game()
            elif choice == '3':
                print("Returning to main menu...")
                main_menu = MainMenu()
                main_menu.display_menu()
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
