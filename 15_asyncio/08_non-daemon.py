import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2) # running on main thread

t = threading.Thread(target=monitor_tea_temp)

t.start()

print("main thread will finish in 2 sec")
