from abc import ABC, abstractmethod

class SudokuUI(ABC):
    @abstractmethod
    def welcome_screen(self):
        """Display a welcome screen and handle user authentication."""
        pass

    @abstractmethod
    def display_main_menu(self):
        """Display the main menu options to the user."""
        pass

    @abstractmethod
    def display_game_board(self, board):
        """Display the game board."""
        pass

    @abstractmethod
    def get_user_input(self):
        """Prompt the user to enter their move."""
        pass

    @abstractmethod
    def display_message(self, message):
        """Display a message to the user."""
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
    def display_highscores(self):
        """Display highscores."""
        pass
