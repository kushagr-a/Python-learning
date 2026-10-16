# ==============================================================================
# MULTITHREADING ON CPU-BOUND TASK (~60 Seconds kyu lagte hain?)
# ==============================================================================
#
# Q: 2 Threads banaye fir bhi time double (~60 sec) kyu laga?
# ------------------------------------------------------------------------------
# 1. CPU-Bound Task:
#    Yeh calculation (10**9 loop) pure CPU-heavy task hai. Isme koi I/O wait ya sleep nahi hai.
#
# 2. Python ka GIL (Global Interpreter Lock):
#    Python (CPython) mein ek rule hai: Chahe aapke computer mein 4 ya 8 CPU cores hon,
#    GIL ek waqt par sirf EK hi thread ko Python code run karne deta hai!
#
# 3. Time Slicing (No True Parallelism):
#    Dono threads alag-alag CPU cores par parallel nahi chal paate.
#    Dono ek hi core par baari-baari (context switch) karke chalte hain:
#    - Thread 1 thoda chalega -> GIL release karega -> Thread 2 thoda chalega -> repeat.
#
# 4. Result:
#    Ek task agar ~30 sec leta hai, toh 2 tasks milkar 30 + 30 = ~60 sec hi lenge
#    (plus thoda extra overhead context switching ka).
#
# GOLDEN RULE:
# Python Multithreading sirf I/O-bound tasks (downloads, file reading) ke liye fast hai,
# CPU-bound tasks (heavy calculations) ke liye Multiprocessing use karni chahiye!
# ==============================================================================

import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += 1
    print("finished crunching number")

start = time.time()

# 2 Threads banaye (Dono same process aur same GIL ke andar phas jaate hain)
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# Threads start kiye
[t.start() for t in threads]

# Threads complete hone ka wait kiya
[t.join() for t in threads]

end = time.time()
print(f"total time taken {end-start:.2f} seconds")