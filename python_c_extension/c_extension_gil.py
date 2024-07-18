import sys
from time import time
from threading import Thread

try:
    from python_c_extension.extension_module import count
except ModuleNotFoundError as e:
    print('Error: extension_module not found. Build extension module by: \n'
          '$ python setup.py build \n'
          'And move the built .so file to the current directory')
    sys.exit(0)


N = int(10e8)

def count_pure_python(n):
    while n > 0:
        n -= 1


def run_count_in_single_thread(count_func=count):
    t1 = time()
    count_func(N)
    time_taken = time() - t1
    return time_taken


def run_count_in_multiple_threads(count_func=count):
    t1 = time()
    th1 = Thread(target=count_func, args=(N // 2,))
    th2 = Thread(target=count_func, args=(N // 2,))
    th1.start(); th2.start()
    th1.join(); th2.join()
    time_taken = time() - t1
    return time_taken


if __name__ == '__main__':
    print('Single Thread (C extension): %8f s' % (run_count_in_single_thread(count)))
    print('Two Threads (C extension):   %8f s' % (run_count_in_multiple_threads(count)))

    print('Single Thread (Pure Python): %8f' % (run_count_in_single_thread(count_pure_python)))
    print('Two Threads (Pure Python):   %8f' % (run_count_in_multiple_threads(count_pure_python)))
