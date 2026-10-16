'''
This script demonstrates a race condition in Python using threading.
A race condition occurs when two or more threads access shared data concurrently,
and at least one of the threads modifies the data, leading to unpredictable results.
'''


import threading

chai_stock = 0;

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

t1 = threading.Thread(target=restock)
t2 = threading.Thread(target=restock)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final stock: {chai_stock}")