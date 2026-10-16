from multiprocessing import Process, Value

def increment(value):
    for i in range(10000):
        with value.get_lock():
            value.value += 1


if __name__ == "__main__":
    value = Value("i", 0)

    processes = [Process(target=increment, args=(value,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(value.value)