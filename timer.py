import time

class Timer:
    def __init__(self):
        self.timer_work = 0.0
        self.timer_break = 0.0
        self.timer_complete = True

    def set_timer(self, preference):
        if (self.timer_complete == False):
            print("You currently still have a task")
            return
        while preference != "pomodoro" and preference != "custom":
            preference = input("Please type either 'pomodoro' or 'custom' ")

        #Right now the timer is in seconds instead of minutes(I did that for testing)
        #When we implement it we can just multiple the number by 60 to turn it into minutes
        if preference == "pomodoro":
            self.timer_work = 25.0
            self.timer_break = 5.0

        if preference == "custom":
            self.timer_work = float(input("How long would you like to work for? "))
            self.timer_break = float(input("How long would you like to take a break for? "))

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
