from time import perf_counter
import asyncio

async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} is ready")


async def main():
    await asyncio.gather(
        brew("Chai"),
        brew("Coffee"),
        brew("Tea"),
        brew("Water")
    )

start = perf_counter()
asyncio.run(main())
end = perf_counter()

print(f"Total time taken: {end-start:.2f} seconds") # :.2f means 2 decimal places
