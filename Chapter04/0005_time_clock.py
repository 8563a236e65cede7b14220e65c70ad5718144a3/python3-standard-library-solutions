"""
Listing 4.5

While time() returns a wall clock time, clock() returns a processor clock
time. The values returned from clock() reflect the actual time used by
the program as it runs
"""
import hashlib
import time


def main():
    # Data to use to calculate sha1 checksums
    data = open(__file__, "rb").read()

    for i in range(5):
        h = hashlib.sha1()
        print(time.ctime(), f": {time.time():0.3f}  {time.clock():0.3f}")
        for i in range(300000):
            h.update(data)
        cksum = h.digest()


if __name__ == "__main__":
    main()
