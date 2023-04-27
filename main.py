from Task_1 import start_task1
from Task_2 import start_task2


print('Do you want the first task or the second ?')
a = input()
if a == '1' or a == "first" or a == "the first":
    start_task1()
if a == '2' or a == "second" or a == "the second":
    start_task2()

