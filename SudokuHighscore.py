import os
import datetime

class Highscore:
    highscore_file = "highscores.txt"

# -----------------------------------------------------------------
    @classmethod
    def get_highscores(cls):
        if not os.path.exists(cls.highscore_file):
            return {}
        with open(cls.highscore_file, 'r') as file:
            lines = file.readlines()
            highscores = {}
            for line in lines:
                username, score = line.strip().split(':')
                highscores[username] = int(score)
            return highscores

# -----------------------------------------------------------------
    @classmethod
    def display_highscores(cls):
        highscores = cls.get_highscores()
        if not highscores:
            print("No highscores available.")
            return
        sorted_highscores = sorted(highscores.items(), key=lambda x: x[1], reverse=True)
        print("\n+++++ Highscores +++++")
        for username, score in sorted_highscores:
            print(f"{username}: {score}")
        print("++++++++++++++++++++++")

# -----------------------------------------------------------------
    @classmethod
    def set_highscore(cls, username, score):
        highscores = cls.get_highscores()
        if username in highscores:
            highscores[username] = max(highscores[username], score)
        else:
            highscores[username] = score
        cls._save_highscores(highscores)

    @classmethod
    def _save_highscores(cls, highscores):
        sorted_highscores = sorted(highscores.items(), key=lambda x: x[1], reverse=True)
        with open(cls.highscore_file, 'w') as file:
            for username, score in sorted_highscores:
                file.write(f"{username}:{score}\n")


# Example usage
# Highscore.set_highscore("User1", 100)
# Highscore.display_highscores()
