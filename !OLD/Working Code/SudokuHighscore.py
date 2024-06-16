import os

class SudokuHighscore:
    HIGHSCORE_FILE = "highscores.txt"

# -----------------------------------------------------------------
    @classmethod
    def get_highscores(cls):
        if not os.path.exists(cls.HIGHSCORE_FILE):
            return []
        highscores = []
        try:
            with open(cls.HIGHSCORE_FILE, 'r') as f:
                for line in f:
                    try:
                        if ':' in line:
                            user, scr = line.strip().split(':')
                            highscores.append((user, int(scr)))
                    except ValueError as e:
                        print(f"Error parsing line '{line.strip()}': {e}")
        except Exception as e:
            print(f"Error reading highscores file: {e}")
        return highscores


# -----------------------------------------------------------------
    @classmethod
    def get_user_highscore(cls, username):
        highscores = cls.get_highscores()
        for user, score in highscores:
            if user == username:
                return score
        return 0


# -----------------------------------------------------------------
    @classmethod
    def display_highscores(cls):
        highscores = cls.get_highscores()
        print("\n+++++ Highscores +++++")
        for user, score in highscores:
            print(f"{user}: {score}")


# -----------------------------------------------------------------
    @classmethod
    def set_highscore(cls, username, score):
        highscores = cls.get_highscores()
        user_found = False
        for i, (user, scr) in enumerate(highscores):
            if user == username:
                highscores[i] = (username, max(scr, score))
                user_found = True
                break
        if not user_found:
            highscores.append((username, score))
        highscores.sort(key=lambda x: x[1], reverse=True)
        with open(cls.HIGHSCORE_FILE, 'w') as f:
            for user, scr in highscores:
                f.write(f"{user}:{scr}\n")
        return score


# -----------------------------------------------------------------
    @classmethod
    def _save_highscores(cls, highscores):
        sorted_highscores = sorted(highscores.items(), key=lambda x: x[1], reverse=True)
        with open(cls.highscore_file, 'w') as file:
            for username, score in sorted_highscores:
                file.write(f"{username}:{score}\n")


# -----------------------------------------------------------------
