import threading
import time

def boil_milk():
    print("Started boiling milk")
    time.sleep(5)
    print("Finished boiling milk")

def make_tea():
    print("Started making tea")
    time.sleep(2)
    print("Finished making tea")

def toast_bread():
    print("Started toasting bread")
    time.sleep(3)
    print("Finished toasting bread")


# start = time.time()

# this is on one main thread so it will run one after another and total time will be sum of all the tasks
# boil_milk()
# make_tea()
# toast_bread()

# end = time.time()
# print(f"total time {end-start:.2f} seconds")


# make thread

# it will start all the tasks at the same time and total time will be the time of the longest task
start = time.time()

t1 = threading.Thread(target=boil_milk, name="BoilMilk")
t2 = threading.Thread(target=make_tea, name="MakeTea")
t3 = threading.Thread(target=toast_bread, name="ToastBread")

# start thread
t1.start()
t2.start()
t3.start()

# join thread
t1.join()
t2.join()
t3.join()

print("All tasks completed")

end = time.time()
print(f"total time {end-start:.2f} seconds")
