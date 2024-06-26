from abc import ABC, abstractmethod

class SudokuUI(ABC):

    @abstractmethod
    def __init__(self, game=None, user=None):
        pass

    @abstractmethod
    def set_game(self, game):
        pass

    @abstractmethod
    def display_welcome_menu(self):
        """Display a welcome screen for user authentication."""
        pass

    @abstractmethod
    def display_main_menu(self):
        """Display the main menu options to the user."""
        pass

    @abstractmethod
    def display_board(self):
        """Display the game board."""
        pass

    @abstractmethod
    def display_pause_menu(self):
        """Display pause menu options."""
        pass

    @abstractmethod
    def display_load_menu(self):
        """Display a menu to load a saved game."""
        pass

    @abstractmethod
    def display_highscore_menu(self):
        """Display highscores."""
        pass

    @abstractmethod
    def display_message(self, message):
        """Display a message to the user."""
        pass

    @abstractmethod
    def get_general_input(self, prompt: str) -> str:
        """Display a prompt and return the user's input as a string."""
        pass

    @abstractmethod
    def get_next_move(self):
        """Prompt the user to enter their move."""
        pass

