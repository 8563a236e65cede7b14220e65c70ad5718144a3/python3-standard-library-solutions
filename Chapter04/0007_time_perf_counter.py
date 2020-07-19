"""
Listing 4.7

A high-resolution monotonic clock is essential for measuring performance.
Determining the best clock data source requires platform-specific
knowledge, which Python provides in perf_counter()

As with monotonic(), the epoch for perf_counter is undefined, and the
values are meant to be used for comparing and computing values, not
as absolute times
"""
import hashlib
import time


def main():
    data = open(__file__, "rb").read()

    loop_start = time.perf_counter()

    for i in range(5):
        iter_start = time.perf_counter()
        h = hashlib.sha1()
        for i in range(300000):
            h.update(data)
        cksum = h.digest()
        now = time.perf_counter()
        loop_elapsed = now - loop_start
        iter_elapsed = now - iter_start
        print(time.ctime(), f": {iter_elapsed:0.3f} {loop_elapsed:0.3f}")


if __name__ == "__main__":
    main()
