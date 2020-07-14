"""
Listing 2.27

Since deques are thread-safe, the contents can even be consumed from both
ends at the same time from separate threads
"""
import collections
import threading
import time


def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print(f"{direction:>8}: {next}")
            time.sleep(1)
    print(f"{direction:>8} done")


def main():
    candle = collections.deque(range(10))
    left = threading.Thread(target=burn,
                            args=("Left", candle.popleft))
    right = threading.Thread(target=burn,
                            args=("Right", candle.pop))

    left.start()
    right.start()

    left.join()
    right.join()


if __name__ == "__main__":
    main()
