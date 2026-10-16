# ==============================================================================
# PROBLEM: Asyncio ke andar BLOCKING (Sync) code kaise chalayein?
# ==============================================================================
#
# 1. Real-world Problem:
#    Maan lo aap ek modern async application bana rahe ho, lekin aapko koi aisi 
#    purani library (jaise requests, legacy database, ya time.sleep) use karni padti 
#    hai jo 'async/await' support nahi karti (Blocking code hai).
#
# 2. Agar seedha call kar diya toh?
#    Asyncio Single-Threaded Event Loop par chalta hai. Agar aapne isme seedha 
#    'time.sleep(3)' chala diya, toh poora Event Loop FREEZE ho jayega aur 
#    baaki saare users/tasks ruk jayenge!
#
# 3. SOLUTION: loop.run_in_executor() + ThreadPoolExecutor
#    Hum blocking kaam ko ek alag "Background Worker Thread" ko de dete hain, 
#    taaki Main Event Loop block na ho aur smoothly chalta rahe!
# ==============================================================================

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# Yeh ek NORMAL (Synchronous/Blocking) function hai (isme async def nahi hai)
def check_stock(item):
    print(f"[Thread] Checking stock for {item}...")
    time.sleep(3)  # Yeh blocking call hai (3 second CPU/thread ko rok kar rakhega)
    return f"[Thread] Checking stock for {item} done"

async def main():
    # 1. Jo Event Loop currently chal raha hai, uska reference liya
    loop = asyncio.get_running_loop()

    # 2. ThreadPoolExecutor: Background threads ka ek pool banaya
    with ThreadPoolExecutor() as pool:
        # 3. loop.run_in_executor(pool, function_name, *arguments):
        #    - 'check_stock' ko background thread mein run hone ke liye bhej diya.
        #    - 'await' lagane se main event loop block nahi hota; wo aaram se doosre 
        #      async tasks chala sakta hai jab tak background thread apna kaam khatam kare.
        result = await loop.run_in_executor(pool, check_stock, "Laptop")
        
        # 4. Result milne par print kiya
        print(result)

# Program start karna
asyncio.run(main())