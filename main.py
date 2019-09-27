import threading
import multiprocessing
import time
from time import time

cores = multiprocessing.cpu_count()
testing_memory = 0
#cores = 4
load = 40000000

def main_thread():
    threads = list()
    load_to_thread = load//cores
    for index in range(cores):
        x = threading.Thread(target=thread_function, args=(load_to_thread,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

def main_process():
    processes = list()
    load_to_thread = load//cores
    for index in range(cores):
        x = multiprocessing.Process(target=thread_function, args=(load_to_thread,))
        processes.append(x)
        x.start()

    for index, process in enumerate(processes):
        process.join()

def thread_function(load):
    i = 0
    while i < load:
        i += 1
        

if __name__ == "__main__":
    start = time()
    main_thread()
    end = time()
    print('threads time',end-start)
    start = time()
    main_process()
    end = time()
    print('process time',end-start)