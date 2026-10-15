import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing")
    count = 0;
    for _ in range(100_000_000):
        count +=1
    print(f"{threading.current_thread().name} finished brewing")

# create thread
t1 = threading.Thread(target=brew_chai, name="Barista-1")
t2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()

# start thread
t1.start()
t2.start()

# join thread
t1.join()
t2.join()

end = time.time()
print(f"total time {end-start:.2f} seconds")