import asyncio

async def brew_chai():
    print("Brewing Chai")
    await asyncio.sleep(2)
    print("Chai is ready")

print("Starting")
asyncio.run(brew_chai())
print("Finished")
