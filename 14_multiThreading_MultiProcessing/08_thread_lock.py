import threading

# ==============================================================================
# Thread Synchronization & Locks: Race Condition & Critical Section
# ==============================================================================

# Shared resource (sab threads isi ek variable ko modify kar rahe hain)
counter = 0

# Lock (Mutex - Mutual Exclusion):
# Ek time par sirf EK hi thread ko critical code execute karne deta hai.
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # ----------------------------------------------------------------------
        # CASE 1: WITHOUT LOCK (Unsafe -> Race Condition ka risk)
        # ----------------------------------------------------------------------
        # "counter += 1" dekhne me 1 step lagta hai, par Python behind-the-scenes
        # isko 3 steps me karta hai:
        #   Step 1 (Read):  counter ki current value memory se read karo (e.g. 5)
        #   Step 2 (Add):   usme +1 karo (5 + 1 = 6)
        #   Step 3 (Write): nayi value memory me wapas save karo (counter = 6)
        #
        # Problem (Race Condition):
        # Agar Thread A aur Thread B dono ne ek hi waqt Step 1 kiya (dono ne dekha counter=5):
        #   - Thread A ne 6 kiya aur save kiya.
        #   - Thread B ne bhi 6 hi save kar diya.
        # Do baar increment hua par count sirf 6 bana (7 hona chahiye tha) -> 1 update lose ho gaya!
        
        counter += 1

        # ----------------------------------------------------------------------
        # CASE 2: WITH LOCK (Thread Safe) -> Uncomment karke use karein
        # ----------------------------------------------------------------------
        # with lock:
        #     counter += 1
        #
        # Lock ka use:
        # 1. Jab ek thread "with lock:" ke andar aata hai, wo lock ko acquire kar leta hai.
        # 2. Jab tak wo release nahi karta, dusra koi bhi thread is block me enter nahi kar sakta (wait karega).
        # 3. Isse guarantee hoti hai ki Read -> Add -> Write bina kisi disturbance ke complete ho.

# Comprehension: 10 threads banaye (har thread 100,000 baar increment karega)
# Expected final value = 10 * 100,000 = 1,000,000 (10 Lakh)
threads = [threading.Thread(target=increment) for _ in range(10)]

# Saare threads start karo
[t.start() for t in threads]

# Saare threads khatam hone ka wait karo
[t.join() for t in threads]

# Final counter print karo
print(f"final counter value : {counter}")

# ==============================================================================
# SUMMARY: Lock kab use karein aur kab nahi?
# ==============================================================================
# - Lock kab OPTIONAL / ZAROORI NAHI hai:
#   Jab threads independent kaam kar rahe hon aur koi SHARED variable update na kar rahe hon
#   (jaise 07_thread_download.py me har thread apni alag image download kar raha tha).
#
# - Lock kab MANDATORY / ZAROORI hai:
#   Jab multiple threads ek hi SHARED data (e.g. counter, bank account balance, inventory)
#   ko ek sath Read aur Write kar rahe hon. Bina lock ke data corrupt hona pakka hai!
# ==============================================================================

