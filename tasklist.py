import datetime
import random

attempts = 0
coins = 0
class Game:
    def __init__(self):
        global attempts
    def rules(self):
        print("Click the button to get a chance to earn coins. 5'%' chance of 20 coins, 70'%' chance of 5, 25'%' chance of 3")
    def roll(self):
        num = random.random()*100
        if (num > 0 and num < 5):
            coins = coins+20
        elif(nums >= 5 and nums < 75):
            coins = coins+5
        else:
            coins = coins+3

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

task_list = TaskList()

tdescription = input("What do you want to do? ")
task_list.add_task("tdescription")
task_list.add_task("Do something")
task_list.add_task("Do another thing")

task_list.print_tasks()

task_list.mark_task_done("Do something")

task_1 = task_list.get_task("Do something")
task_2 = task_list.get_task("Do another thing")

task_list.print_tasks()

if task_1:
    print(f"Task 1 - Time: {task_1.time}, Task: {task_1.task_des}")
else:
    print("Task 'Do something' not found")

if task_2:
    print(f"Task 2 - Time: {task_2.time}, Task: {task_2.task_des}")
else:
    print("Task 'Do another thing' not found")

print(coins)