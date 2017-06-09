#!/usr/bin/python
from threading import Thread

x = 0

def inc():
    global x
    x += 1

def dec():
    global x
    x -= 1

threads = []

for i in range(1, 10000):
    threads.append(Thread(target=inc))
    threads.append(Thread(target=dec))

for th in threads:
    th.start()

for th in threads:
    th.join()

print(x)