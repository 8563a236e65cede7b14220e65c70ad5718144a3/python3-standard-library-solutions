"""
Listing 2.58

Sometimes the processing order of the items in a queue needs to be based
on characteristics of those items, rather than just the order they are
created or added to the queue. PriorityQueue uses the sort order of the
contents of the queue to decide which item to retrieve
"""
import functools
import queue
import threading

@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print("New job:", description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


def process_job(q):
    while True:
        next_job = q.get()
        print("Processing job: ", next_job.description)
        q.task_done()


def main():
    q = queue.PriorityQueue()

    q.put(Job(3, "Mid-level job"))
    q.put(Job(10, "Low-level job"))
    q.put(Job(1, "Important job"))

    workers = [
        threading.Thread(target=process_job, args=(q,)),
        threading.Thread(target=process_job, args=(q,))
    ]

    for w in workers:
        w.setDaemon(True)
        w.start()

    q.join()


if __name__ == "__main__":
    main()
