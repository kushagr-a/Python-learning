
'''
This script demonstrates a deadlock in Python using threading.
A deadlock occurs when two or more threads are blocked forever,
waiting for each other to release resources they need.
'''

import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def  task1():
    with lock_a:
        print("Task 1 acquired lock A")
        with lock_b:
            print("Task 1 acquired lock B")

def task2():
    with lock_b:
        print("Task 2 acquired lock B")
        with lock_a:
            print("Task 2 acquired lock A")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

print("Both tasks completed.")