import time
import datetime

class TimeTask:
    def __init__(self):
        self.dt_start = datetime.datetime.now()
        print(self.dt_start)

    def end(self):
        self.dt_end = datetime.datetime.now()
        return self.dt_end - self.dt_start

task = TimeTask()
time.sleep(95)
time = task.end()
print(time)
