from timer import Timer
from tasklist import Game1, Task, TaskList
import time

t1 = Timer()
t1.set_timer
t1.start_time
t1.finish_timer

if t1.finish_timer:
    t1.more_attempts(1)

task_list = TaskList()

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

print(coins)