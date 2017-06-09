from threading import Thread
import matplotlib.pyplot as plt
import time
import tqdm


def count(n):
    while n > 0:
        n -= 1


def run_count_single_thread(N):
    t0 = time.time()
    count(N)
    t = time.time() - t0
    print("Single: %8f" % t)
    return t


def run_count_multithread(N):
    t1 = Thread(target=count, args=(N//2,))
    t2 = Thread(target=count, args=(N//2,))
    t0 = time.time()
    t1.start(); t2.start()
    t1.join(); t2.join()
    t = time.time() - t0
    print("Double: %8f" % t)
    return t

def main():
    N = int(10e17)

    time_span_single = []
    time_span_multiple = []
    no_count = []

    for i in tqdm.tqdm(range(int(10e4), int(10e5), int(10e4))):
        no_count.append(i)
        print(i)
        time_span_single.append(run_count_single_thread(i))
        time_span_multiple.append(run_count_multithread(i))

    plt.plot(time_span_single, no_count)
    plt.plot(time_span_multiple, no_count)
    plt.show()


main()