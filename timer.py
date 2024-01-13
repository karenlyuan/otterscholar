class Timer:
    def __init__():
        preference = input("Would you like to use the pomodoro method or set a custom timer?")
        timer_work = 0
        timer_break = 0

    def set_timer(preference):
        while preference != "pomodoro" and preference != "custom":
            preference = input("Please type either 'pomodoro' or 'custom'")

        if preference == "pomodoro":
            timer_work = 25
            timer_break = 5

        if preference == "custom":
            timer_work = input("How long would you like to work for?")
            timer_break = input("How long would you like to take a break for?")