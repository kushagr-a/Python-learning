# ==============================================================================
#                     PYTHON MULTIPROCESSING (Step-by-Step)
# ==============================================================================

# 1. Imports
# - Process: Naya Operating System process create karne ke liye.
#   Har process ka apna ALAG Memory space aur ALAG Python Interpreter (GIL) hota hai.
from multiprocessing import Process
import time

# ------------------------------------------------------------------------------
# 2. Worker Function
# ------------------------------------------------------------------------------
def brew_chai(name):
    """
    Ye function chai banane ka kaam karta hai.
    Har chai banne me 3 seconds lagte hain.
    """
    print(f"start of {name} chai brewing")
    time.sleep(3)  # Chai ubalne me 3 second lag rahe hain
    print(f"end of {name} chai brewing")


# ------------------------------------------------------------------------------
# 3. Main Protection Guard: if __name__ == '__main__':
# ------------------------------------------------------------------------------
# ⚠️ BOHOT ZAROORI (INTERVIEW QUESTION):
# Windows par multiprocessing karte waqt ye line MANDATORY (zaroori) hoti hai!
# Kyun?
# Kyunki Windows naye process banate waqt puri script ko dobara import/read karta hai.
# Agar ye 'if' condition nahi hogi, toh child process bhi naye child process
# banata rahega aur infinite loop (crash / RuntimeError) ho jayega.
if __name__ == '__main__':

    # --------------------------------------------------------------------------
    # 4. Creating Multiple Processes (List Comprehension se)
    # --------------------------------------------------------------------------
    # Yaha hum 3 alag-alag Processes bana rahe hain.
    # target=brew_chai : Kaun sa function chalana hai.
    # args=(f"chai #{i+1}",) : Function ko arguments tuple me pass karne hote hain.
    #   (DHYAN DEIN: Single argument ke baad comma ',' lagana zaroori hai
    #    warna Python use tuple nahi samjhega!)
    chai_maker = [
        Process(target=brew_chai, args=(f"chai #{i+1}",))
        for i in range(3)
    ]

    # --------------------------------------------------------------------------
    # 5. Start all processes (Hardware Cores par run karna)
    # --------------------------------------------------------------------------
    # Har process ko start karte hain:
    # OS in teeno processes ko CPU ke alag-alag cores par simultaneously execute karega.
    # (True Parallelism!)
    for p in chai_maker:
        p.start()
    
    # --------------------------------------------------------------------------
    # 6. Wait for all to complete (p.join())
    # --------------------------------------------------------------------------
    # p.join() ka matlab:
    # Main script ko bolo rukne ke liye jab tak saare child processes apna kaam khatam na kar lein.
    # Agar join() nahi lagayenge, toh 'All chai are ready!' turant print ho jayega.
    for p in chai_maker:
        p.join()

    # --------------------------------------------------------------------------
    # 7. Final Completion
    # --------------------------------------------------------------------------
    # Saari 3 chai parallel ban gayi!
    # Normal execution me: 3 chai * 3 sec = 9 seconds lagte.
    # Multiprocessing me: Teeno ek sath bani, toh kul ~3 seconds hi lage!
    print("All chai are ready!")

    # --------------------------------------------------------------------------
    # 💡 BONUS KNOWLEDGE (Output Order ke baare me):
    # Kabhi chai #2 pehle print hoti hai, kabhi #1 ya #3. Kyun?
    # Kyunki teeno processes independent hain! OS ka scheduler decide karta hai
    # ki kis core par kaun sa process microsecond pehle execute hoga.
    # --------------------------------------------------------------------------