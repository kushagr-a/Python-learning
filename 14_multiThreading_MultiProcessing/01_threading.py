# ==============================================================================
#                      PYTHON MULTITHREADING (Step-by-Step)
# ==============================================================================

# 1. Imports
import threading  # Multi-threading ke liye Python ka built-in module
import time       # Execution me delay (waiting time) simulate karne ke liye

# ------------------------------------------------------------------------------
# 2. Worker Functions (Wo kaam jo alag-alag threads karenge)
# ------------------------------------------------------------------------------

def take_order():
    """
    Ye function customer se order lene ka kaam karta hai.
    Har order lene me 1 second ka delay (sleep) lagta hai.
    """
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        # time.sleep(1) -> 1 second ka pause (waiting time).
        # Jab ye thread sleep kar raha hota hai, CPU idle nahi baithta,
        # wo doosre thread (brew_chai) par switch ho jata hai (Concurrency).
        time.sleep(1)

def brew_chai():
    """
    Ye function chai banane ka kaam karta hai.
    Har chai ubalne me 2 second lagte hain (zyada time-consuming kaam).
    """
    for i in range(1, 4):
        print(f"Brewing chai #{i}")
        # 2 second ka waiting time (jaise gas pe chai ubal rahi ho)
        time.sleep(2)

# ------------------------------------------------------------------------------
# 3. Thread Creation (Kaam assign karna)
# ------------------------------------------------------------------------------
# Yaha hum 2 alag threads create kar rahe hain:
# - target=take_order : Is thread ko bataya ki kaun sa function execute karna hai.
#   (Note: Sirf function ka naam pass karte hain, take_order() parenthesis nahi lagate!)
t1 = threading.Thread(target=take_order)  # Thread 1: Order lene ka kaam
t2 = threading.Thread(target=brew_chai)   # Thread 2: Chai banane ka kaam

# ------------------------------------------------------------------------------
# 4. Start Threads (Execution shuru karna)
# ------------------------------------------------------------------------------
# .start() call karte hi dono threads background me ek sath run hona shuru ho jate hain.
t1.start()
t2.start()

# ------------------------------------------------------------------------------
# 5. Join Threads (Intezar karna jab tak dono threads khatam na ho jayein)
# ------------------------------------------------------------------------------
# .join() ka matlab: "Main program ko bolo yahan ruk jaye jab tak ye thread poora na ho jaye."
# Agar .join() nahi lagayenge, toh 'All orders are ready!' pehle hi print ho jayega,
# jabki background me order lena aur chai banna chal hi raha hoga.
t1.join()  # Main thread rukega jab tak t1 (take_order) poora na ho jaye
t2.join()  # Main thread rukega jab tak t2 (brew_chai) poora na ho jaye

# ------------------------------------------------------------------------------
# 6. Final Statement
# ------------------------------------------------------------------------------
# Ye line tabhi execute hogi jab t1 aur t2 dono threads successfully complete ho chuke honge.
print("All orders are ready!")