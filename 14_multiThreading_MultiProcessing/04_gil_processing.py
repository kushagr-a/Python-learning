from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for i in range(100_000_000):
        count +=1
    print(f"Finished the count process...")

# # create process
# p1 = Process(target=crunch_number, name="Processor-1")
# p2 = Process(target=crunch_number, name="Processor-2")

# start = time.time()

# # start process
# p1.start()
# p2.start()

# # join process
# p1.join()
# p2.join()

# end = time.time()
# print(f"total time {end-start:.2f} seconds")

if __name__ == "__main__": # this is used for multiprocessing otherwise it will run the code again and again or run into infinite loop
    # create process
    p1 = Process(target=crunch_number, name="Processor-1")
    p2 = Process(target=crunch_number, name="Processor-2")

    start = time.time()

    # start process
    p1.start()
    p2.start()

    # join process
    p1.join()
    p2.join()

    end = time.time()
    print(f"total time {end-start:.2f} seconds")