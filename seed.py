import os


class Seed:
    def __init__(self, path, seed_id, coverage, exec_time):
        self.path = path
        self.seed_id = seed_id
        self.coverage = coverage
        self.exec_time = exec_time
        # by default, a seed is not marked as favored
        self.favored = 0
        self.priority = "inf"
        self.used_in_cycle = False

    def mark_favored(self):
        self.favored = 1

    def unmark_favored(self):
        self.favored = 0

    def get_file_size(self):
        return os.path.getsize(self.path)
