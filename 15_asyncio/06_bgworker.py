import asyncio
import threading
import time

def backgoundWorker():
    count = 0
    while True:
        time.sleep(1)
        print(f"Logging the system health every second...")

async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(5)
    print("Orders fetched")

async def main():
    # Create a background worker thread
    bg_thread = threading.Thread(target=backgoundWorker, daemon=True)
    bg_thread.start()

    # Fetch orders
    await fetch_orders()

asyncio.run(main())