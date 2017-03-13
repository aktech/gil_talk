import pyximport
pyximport.install()

import time
from threading import Thread
import parpyx

N = 999999999

t0 = time.time()
parpyx.busy_sleep(N)
parpyx.busy_sleep(N)
parpyx.busy_sleep(N)
print('Time without Threading : %.8f' % (time.time() - t0))

t0 = time.time()
t1 = Thread(target=parpyx.busy_sleep_nogil, args=(N, ))
t2 = Thread(target=parpyx.busy_sleep_nogil, args=(N, ))
t3 = Thread(target=parpyx.busy_sleep_nogil, args=(N, ))

t1.start(); t2.start(); t3.start()
t1.join(); t2.join(); t3.join()
print('Time with Threading    : %.8f' % (time.time() - t0))
