import time

class SudokuStopwatch:
# -----------------------------------------------------------------
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0


# -----------------------------------------------------------------
    def start(self):
        if self.start_time is None:
            self.start_time = time.time()


# -----------------------------------------------------------------
    def pause(self):
        if self.start_time is not None:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None


# -----------------------------------------------------------------
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0


# -----------------------------------------------------------------
    def get_elapsed_time(self):
        if self.start_time is not None:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time

# -----------------------------------------------------------------
