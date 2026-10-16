# ==============================================================================
# ASYNCIO + PROCESSPOOLEXECUTOR (CPU-Bound / Heavy Computation Tasks)
# ==============================================================================
#
# 1. ThreadPoolExecutor vs ProcessPoolExecutor:
#    - ThreadPoolExecutor (04_thread_async.py): I/O blocking tasks (sleep, legacy DB, files).
#    - ProcessPoolExecutor (05_async_process.py): CPU-heavy tasks (Encryption, Hashing, 
#      Image/Video processing, Machine Learning, Heavy Math).
#
# 2. Process kyu use kiya?
#    Heavy calculation (jaise encryption) karte waqt CPU 100% engage hota hai.
#    Agar hum thread use karenge toh Python ka GIL baaki sabhi tasks ko rok dega.
#    ProcessPoolExecutor is kaam ko ek ALAG CPU CORE aur alag Python process par 
#    bhej deta hai, jisse Main Async Event Loop bilkul free aur responsive rehta hai!
#
# 3. Windows Requirement:
#    'if __name__ == "__main__":' lagana mandatory hai, varna Windows par child 
#    processes infinite loop mein crash ho jayenge (spawn method).
# ==============================================================================

import asyncio
from concurrent.futures import ProcessPoolExecutor

# Yeh ek CPU-intensive function hai (e.g. Data Encryption)
def encrypt(data):
    # Asli world me yahan heavy mathematical algorithms (AES, RSA, etc.) chalte hain
    return f"*** encrypted data of {data} ***"

async def main():
    # 1. Jo Event Loop currently chal raha hai, uska reference liya
    loop = asyncio.get_running_loop()

    # 2. ProcessPoolExecutor: OS-level ke alag child processes banata hai
    with ProcessPoolExecutor() as pool:
        # 3. loop.run_in_executor():
        #    - 'encrypt' function ko alag CPU core/process par bhej diya.
        #    - 'await' laga hai taaki result aane tak Event Loop baaki async tasks handle kare.
        result = await loop.run_in_executor(pool, encrypt, "credit_card_info")
        
        print("Processing data in background processes...")
        print(f"Credit Card Info Encrypted: {result}")

# Program start (Windows multiprocessing safety ke liye zaroori hai)
if __name__ == "__main__":
    asyncio.run(main())
