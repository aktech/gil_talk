import time
import threading


TOTAL_WORK = 10000000

class CountdownThread(threading.Thread):

    def __init__(self,count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            self.count -= 1
        return

start = time.time()

# countdown(TOTAL_WORK)
thread_1 = CountdownThread(TOTAL_WORK//2)  # Create the thread object
thread_2 = CountdownThread(TOTAL_WORK//2)  # Create another thread

thread_1.start(); thread_2.start()
thread_1.join(); thread_2.join()

end = time.time()

print(end - start)