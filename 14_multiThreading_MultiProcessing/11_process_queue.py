import __main__
from multiprocessing import Process, Queue, Value

def prepare_chai(queue):
    queue.put("Chai is ready")


if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()

    print( queue.get())