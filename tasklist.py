import datetime
import random
from timer import Timer

attempts = 0
coins = 0

class Game1:
    def __init__(self):
        global attempts

    def rules(self):
        print("Click the button to get a chance to earn coins. 1'%' chance of 100 coins, 5'%' chance of 20 coins, 75'%' chance of 5, 19'%' chance of 3")
    
    def roll(self):
        global attempts
        global coins
        #When implementing on tk, show the number of coins earned each roll
        if attempts > 0:
            attempts = attempts - 1
            num = random.random() * 100.0
            if  0 <= num < 1:
                coins += 50
                print("50 coins!")
            if 1 <= num < 6:
                coins += 20
                print("20 coins!")
            elif 6 <= num < 81   :
                coins += 5
                print("5 coins!")
            else:
                coins += 3
                print("3 coins!")
        else:
            print("Not enough attempts, finish tasks to get more")
    def print_coins(self):
        global coins
        print(coins)

class Task:
    def __init__(self, time, task_des):
        self.time = time
        self.task_des = task_des

class TaskList:
    def __init__(self):
        self.task_dict = {}

    def add_task(self, task_des, time=datetime.datetime.now()):
        new_task = Task(time, task_des)
        self.task_dict[task_des] = new_task

    def get_task(self, task_des):
        return self.task_dict.get(task_des, None)

    # Will be a button in tkinker, when button is pressed, execute this
    def mark_task_done(self, task_des):
        del self.task_dict[task_des]
        global attempts
        attempts = attempts+1

    def print_tasks(self):
        if self.task_dict:
            for task_des, task_instance in self.task_dict.items():
                print(f"Task - Time: {task_instance.time}, Description: {task_instance.task_des}")
        else:
            print("No tasks found.")

"""task_list = TaskList()

tdescription = input("What do you want to do? ")
task_list.add_task(tdescription)
task_list.add_task("Do something")
task_list.add_task("Do another thing")

task_list.print_tasks()

task_list.mark_task_done("Do something")

task_1 = task_list.get_task("Do something")
task_2 = task_list.get_task("Do another thing")

task_list.print_tasks()


#if task_1:
 #   print(f"Task 1 - Time: {task_1.time}, Task: {task_1.task_des}")
#else:
 #   print("Task 'Do something' not found")

#if task_2:
 #   print(f"Task 2 - Time: {task_2.time}, Task: {task_2.task_des}")
#else:
 #   print("Task 'Do another thing' not found")

print(coins)

game = Game1()
game.rules()
game.roll()
game.roll()

print(coins)"""