import time

class Timer:
    def __init__(self):
        self.timer_work = 0.0
        self.timer_break = 0.0
        self.timer_complete = True

    def set_pomodoro_timer(self):
        if not self.timer_complete:
            print("You currently still have a task")
            return

        self.timer_work = 25*60
        self.timer_break = 5.0*60
        self.timer_complete = False

    def set_custom_timer(self, work_duration, break_duration):
        if not self.timer_complete:
            print("You currently still have a task")
            return

        self.timer_work = work_duration
        self.timer_break = break_duration
        self.timer_complete = False

    def start_timer(self):
        time.time()
        print("Time to starting working!")
        time.sleep(self.timer_work)
        time.time()
        print("Time for your break! Good job, you earned it!")
        time.sleep(self.timer_break)
        time.time()

    def finish_timer(self):
        self.timer_complete = True
