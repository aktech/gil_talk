def busy_sleep(int n):
    _busy_sleep(n)


def busy_sleep_nogil(int n):
    with nogil:
        _busy_sleep(n)


cdef inline void _busy_sleep(double n) nogil:
    cdef double tmp = 0.0

    while n > 0:
        # Do some CPU intensive useless computation to waste some time
        tmp = (n ** 0.5) ** 0.5
        n -= 1
