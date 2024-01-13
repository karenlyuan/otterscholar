import time

class Timer:
    def __init__(self):
        preference = input("Would you like to use the pomodoro method or set a custom timer?")
        timer_work = 0
        timer_break = 0
        timer_complete = False
        attempts = 0

    def set_timer(self, preference):
        while preference != "pomodoro" and preference != "custom":
            preference = input("Please type either 'pomodoro' or 'custom'")

        if preference == "pomodoro":
            timer_work = 25
            timer_break = 5

        if preference == "custom":
            timer_work = input("How long would you like to work for?")
            timer_break = input("How long would you like to take a break for?")

    def start_time(self, timer_work, timer_break):
        time.time()
        print("Time to starting working!")
        time.sleep(timer_work)
        time.time()
        print("Time for your break! Good job, you earned it!")
        time.sleep(timer_break)
        time.time()

    def finish_timer(self):
        timer_complete = True

    def more_attempts(self, num):
        attempts += num