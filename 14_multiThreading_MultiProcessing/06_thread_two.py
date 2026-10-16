import threading
import time

def prepare_chai(type_, wait_time):
    """Prepares a cup of chai of given type and waits for the given time"""
    print(f"Started preparing {type_} chai")
    time.sleep(wait_time)
    print(f"Finished preparing {type_} chai")

# ==============================================================================
# 1. NORMAL FUNCTION CALL (Sequential / Synchronous Execution) -> 15 Seconds
# ==============================================================================
# - Kyu 15 sec lagte hain?
#   1. Ye Single Thread (Main Thread) pe line-by-line (ek ke baad ek) execute hota hai.
#   2. Pehle "Ginger" chai banegi aur 5 sec wait karegi (poora program block ho jata hai).
#   3. Jab "Ginger" complete hogi, tab "Masala" start hogi (aur 5 sec legi).
#   4. Uske baad "Elaichi" start hogi (aur 5 sec legi).
#   5. Total Time = 5 + 5 + 5 = 15 seconds (Sum of all wait times).

# start = time.time()
# prepare_chai("Ginger", 5)
# prepare_chai("Masala", 5)
# prepare_chai("Elaichi", 5)
# end = time.time()
# print(f"total time of function call {end-start:.2f} seconds")


# ==============================================================================
# 2. MULTITHREADING (Concurrent Execution) -> ~5 Seconds
# ==============================================================================
# - Kyu ~5 sec lagte hain?
#   1. Har task ke liye alag thread banaya (t1, t2, t3).
#   2. Note: Threads same memory space share karte hain, par independently kaam karte hain.
#   3. Jab `t.start()` kiya, to teeno threads lagbhag ek saath (concurrently) shuru ho gaye.
#   4. Jab ek thread `time.sleep()` me wait kar raha hota hai (I/O wait), CPU idle nahi baithta,
#      Python dusre thread ko switch/start kar deta hai.
#   5. Teeno chai ek hi saath 5-5 second ke liye ban rahi hain (overlapping time).
#   6. `t.join()` ensure karta hai ki Main Thread tab tak wait kare jab tak sabhi threads complete na ho jayein.
#   7. Total Time = Max wait time of all threads = ~5 seconds (na ki 5+5+5=15).

start = time.time()

# Threads create karna
t1 = threading.Thread(target=prepare_chai, args=("Ginger", 5))
t2 = threading.Thread(target=prepare_chai, args=("Masala", 5))
t3 = threading.Thread(target=prepare_chai, args=("Elaichi", 5))

# Threads start karna (Background me kaam shuru)
t1.start()
t2.start()
t3.start()

# join() ka matlab: Main thread wait karega jab tak t1, t2, t3 apna kaam khatam na kar lein
t1.join()
t2.join()
t3.join()

print("All tasks completed")

end = time.time()
print(f"total time of thread {end-start:.2f} seconds")