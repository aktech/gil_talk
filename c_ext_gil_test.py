from extension_module import count
from time import time
from threading import Thread

N = int(10e8)

# Single Threads
t1 = time()
count(N)
print('Single Thread: %8f' % (time() - t1))

# Two Threads
t1 = time()
th1 = Thread(target=count, args=(N//2,))
th2 = Thread(target=count, args=(N//2,))
th1.start(); th2.start()
th1.join(); th2.join()
print('Two Threads:   %8f' % (time() - t1))
