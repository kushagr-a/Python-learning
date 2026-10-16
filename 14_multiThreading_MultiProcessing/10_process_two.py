# ==============================================================================
# MULTIPROCESSING ON CPU-BOUND TASK (~30 Seconds kyu lagte hain?)
# ==============================================================================
#
# Q: Threading ne ~60 sec liye, par Multiprocessing ne sirf ~30 sec kyu liye?
# ------------------------------------------------------------------------------
# 1. Independent Python Interpreters & GIL:
#    Har process ka apna alag Python Interpreter aur apna khud ka alag GIL hota hai.
#    Ek process ka GIL dusre process ko block NAHI karta!
#
# 2. True Parallelism (Multi-core CPU ka asli use):
#    Operating System (OS) dono processes ko alag-alag CPU Cores par daal deta hai:
#    - Process 1 -> Core 0 par chalta hai (30 seconds)
#    - Process 2 -> Core 1 par chalta hai (30 seconds)
#    Dono calculations EK HI SAMAY (simultaneously) hardware level pe chalte hain!
#
# 3. Independent Memory Space:
#    Har process ki apni alag memory aur virtual memory hoti hai.
#    Variables ki copy alag hoti hai, isliye yahan direct Race Condition ka jhamela nahi hota.
#
# 4. Result:
#    Dono processes ek sath shuru hote hain aur lagbhag ek sath ~30 sec me khatam ho jaate hain.
#    Total time = Longest process ka time = ~30 to 32 seconds (Half of Threading)!
#
# Note on Windows: "if __name__ == '__main__':" lagana zaroori hai taaki child processes
# baar-baar poori script ko re-import karke infinite processes na banayein (spawn method).
# ==============================================================================

from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += 1
    print("finished crunching number")

if __name__ == "__main__":
    start = time.time()

    # 2 alag-alag Processes create kiye (Har process ke paas apna Core & GIL hoga)
    process = [Process(target=cpu_heavy) for _ in range(2)]

    # Processes start kiye (Alag-alag CPU cores par parallel chalna shuru)
    [p.start() for p in process]

    # Main process wait karega jab tak dono child processes finish na ho jayein
    [p.join() for p in process]

    end = time.time()
    print(f"total time taken {end-start:.2f} seconds")