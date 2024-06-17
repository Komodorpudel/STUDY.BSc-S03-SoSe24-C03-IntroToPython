import tkinter as tk
from tkinter import simpledialog, messagebox

class SudokuGUI(SudokuUI):

# -----------------------------------------------------------------
    def __init__(self, game=None, user=None):
        self.game = game
        self.user = user


# -----------------------------------------------------------------
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.setup_welcome_screen()

    def setup_welcome_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Sudoku!").pack()
        username = simpledialog.askstring("Username", "Enter your username:")
        password = simpledialog.askstring("Password", "Enter your password:", show='*')
        self.display_main_menu()

    def display_main_menu(self):
        self.clear_screen()
        tk.Button(self.root, text="Start New Game", command=self.display_game_board).pack()
        tk.Button(self.root, text="Load Game", command=self.display_load_menu).pack()
        tk.Button(self.root, text="View Highscores", command=self.display_highscores).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def display_board(self):
        self.clear_screen()
        # Display the board here

    def get_user_input(self):
        return simpledialog.askstring("Input", "Enter your move (row col num):")

    def display_message(self, message):
        messagebox.showinfo("Message", message)

    def display_pause_menu(self):
        self.clear_screen()
        tk.Button(self.root, text="Resume Game", command=self.display_game_board).pack()
        tk.Button(self.root, text="Save Game", command=lambda: self.display_message("Save Game not implemented")).pack()
        tk.Button(self.root, text="Quit to Main Menu", command=self.display_main_menu).pack()

    def display_load_menu(self):
        self.clear_screen()
        # Implementation for load menu

    def display_highscore_menu(self):
        self.clear_screen()
        # Implementation for displaying highscores

    def clear_screen(self):
        for widget in self.root
