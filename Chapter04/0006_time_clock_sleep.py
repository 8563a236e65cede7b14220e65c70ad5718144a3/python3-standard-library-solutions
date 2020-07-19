"""
Listing 4.6

Typically, the processor clock does not tick if a program is not doing
anything

Calling sleep() yields control from the current thread and asks that
thread to wait for the system to wake it back up. If a program has one
thread only, this function effectively blocks the app so that it does
no work
"""
import time


def main():
    template = "{} - {:0.2f} - {:0.2f}"
    print(template.format(
        time.ctime(), time.time(), time.clock()
    ))

    for i in range(3, 0, -1):
        print("Sleeping", i)
        time.sleep(i)
        print(template.format(
            time.ctime(), time.time(), time.clock()
        ))


if __name__ == "__main__":
    main()
