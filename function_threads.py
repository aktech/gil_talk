import time
import threading

TOTAL_WORK = 10000000


def countdown(count):
    while count > 0:
        count -= 1


# Single Thread
start = time.time()
countdown(TOTAL_WORK)
print('Single Thread: %8f' % (time.time() - start))

# Two Threads
thread1 = threading.Thread(target=countdown, args=(TOTAL_WORK / 2,))
thread2 = threading.Thread(target=countdown, args=(TOTAL_WORK / 2,))

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('Two Threads:   %8f' % (time.time() - start))
