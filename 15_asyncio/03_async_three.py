import time
import asyncio
import aiohttp

'''
like Blocking --> time.sleep(2)
like Non-Blocking --> asyncio.sleep(2)

'''

async def fetch(session, url):
    async with session.get(url) as response:
        print(f"Status from {url}: {response.status}")


async def main():
    urls = ["https://httpbin.org/delay/4"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        # task = [t1, t2, t3]
        await asyncio.gather(*tasks) # this astric task used to give multiple tasks to gather 


start = time.time()
asyncio.run(main())
end = time.time()

print(f"Total time taken: {end-start:.2f} seconds")
        
