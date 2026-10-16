'''
 daemon ->  daemon thread ek  aese thread ko bolte hain jo main thread se pehle kabhi bnde nhi ho skta. mtlb agar main thread end ho jata hai
 toh demon thread bhi automatically end ho jata hai even ki agar uska kaam pura na bhi hua ho.

 non daemon -> non daemon thread ka kaam pure hone ke baad main thread end ho jata hai. 

'''

import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2) # running on main thread

t = threading.Thread(target=monitor_tea_temp, daemon=True)

t.start()

print("main thread will finish in 2 sec")
