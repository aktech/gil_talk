import sys
from time import time
from threading import Thread

try:
    from extension_module import count
except ModuleNotFoundError as e:
    print('Error: extension_module not found. Build extension module by: \n'
          '$ python setup.py build \n'
          'And move the built .so file to the current directory')
    sys.exit(0)


N = int(10e8)


def run_count_in_single_thread():
    t1 = time()
    count(N)
    time_taken = time() - t1
    return time_taken


def run_count_in_multiple_threads():
    t1 = time()
    th1 = Thread(target=count, args=(N // 2,))
    th2 = Thread(target=count, args=(N // 2,))
    th1.start(); th2.start()
    th1.join(); th2.join()
    time_taken = time() - t1
    return time_taken


if __name__ == '__main__':
    print('Single Thread: %8f' % (run_count_in_single_thread()))
    print('Two Threads:   %8f' % (run_count_in_multiple_threads()))
