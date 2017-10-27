import time
import datetime

class Time:
    def __init__(self):
        self.start_time = self.start()
        self.dt_start = datetime.datetime.now()

    def start(self):
        return time.time()

    def end(self):
        self.dt_end = datetime.datetime.now()
        return time.time()

    def cur()
        self.end_time = self.end()
        self.cur_time = self.end_time - self.start_time
        return self.cur_time
