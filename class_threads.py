# coding=utf-8

import time
import threading

TOTAL_WORK = 10000000


class CountdownThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            self.count -= 1
        return


start = time.time()
single_thread = CountdownThread(TOTAL_WORK // 2)
single_thread.start()
single_thread.join()
end = time.time()
print('Single Thread: ', end - start)


start = time.time()

# countdown(TOTAL_WORK)
thread_1 = CountdownThread(TOTAL_WORK // 2)  # Create the thread object
thread_2 = CountdownThread(TOTAL_WORK // 2)  # Create another thread

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

end = time.time()
print('Two Threads: ', end - start)
