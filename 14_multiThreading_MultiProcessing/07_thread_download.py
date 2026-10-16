import threading 
import requests
import time

# ==============================================================================
# Network Download Example: I/O-Bound Task (CPU wait karta hai network response ka)
# ==============================================================================

def downlad_image(url):
    print(f"started downloading image from {url}")
    # Network request (I/O wait): is time CPU idle rehta hai
    resp = requests.get(url)
    print(f"finished downloading image from {url}")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

# ------------------------------------------------------------------------------
# 1. MULTITHREADING (Concurrent Execution) -> Faster (~1.5 sec)
# ------------------------------------------------------------------------------
# Kyu fast hai? 
# Teeno images ka download ek saath (concurrently) shuru ho jata hai.
# Jab ek image network se download ho rahi hoti hai, baaki threads bhi parallel download ho rahe hote hain.
start = time.time()

threads = []

# Har URL ke liye ek alag thread banakar start kiya
for url in urls:
    t = threading.Thread(target=downlad_image, args=(url,))
    t.start()          # Background me download shuru
    threads.append(t)

# join() -> Main thread tab tak wait karega jab tak saare downloads complete na ho jayein
for t in threads:
    t.join()

end = time.time()
print(f"total time of multithreading {end-start:.2f} seconds\n")


# ------------------------------------------------------------------------------
# 2. NORMAL FUNCTION CALL (Sequential Execution) -> Slower (~3.3+ sec)
# ------------------------------------------------------------------------------
# Kyu slow hai?
# Ek ke baad ek download hota hai. 
# Pehli image download hogi -> complete hogi -> tab dusri shuru hogi -> fir teesri.
# Total time = teeno download times ka sum (1.1 + 1.1 + 1.1 ≈ 3.3 sec)
start = time.time()

for url in urls:
    downlad_image(url)

end = time.time()
print(f"total time of normal function call {end-start:.2f} seconds")