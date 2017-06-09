from threading import Thread
import random
import time

X = 0

def change_X_p():
    global X
    X += 1


def change_X_n():
    global X
    X -= 1


def func(n, f):
    for i in range(1, n):
        f()

t1 = Thread(target=func, args=(10000, change_X_p))
t2 = Thread(target=func, args=(10000, change_X_n))
print(X)
t1.start()
t2.start()
t1.join()
t2.join()
print(X)

# threads = []
# N = 100000

# for i in range(N):
#     threads.append(Thread(target=change_X, args=()))
#     threads[i].start()

# for i in range(N):
#     threads[i].join()