"""
Listing 2.59

This example demonstrates how to use the Queue class with multiple
threads. The program reads one or more RSS feeds, queues up the
enclosures for the five most recent episodes from each feed to be downloaded,
and processes sever downloads in parallel using threads.

* conda install feedparser
"""
import queue
import threading
import time
import urllib
import urllib.parse

import feedparser

# Set up some global variables
num_fetch_threads = 2
enclosure_queue = queue.Queue()
feed_urls = [
    "http://talkpython.fm/episodes/rss"
]


def message(s):
    print(f"{threading.current_thread().name}: {s}")


def download_enclosures(q):
    """
    This is the worker thread function.
    It processes items in the queue one after
    another. These daemon threads go into an
    infinite loop and exit only when the main
    thread ends
    :param q:
    :return:
    """
    while True:
        message("look for for the next enclosure")
        url = q.get()
        filename = url.rpartition("/")[-1]
        message(f"downloading {filename}")
        response = urllib.request.urlopen(url)
        data = response.read()
        message(f"writing to {filename}")
        with open(filename, "wb") as outfile:
            outfile.write(data)
        q.task_done()


def main():
    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target=download_enclosures,
            args=(enclosure_queue,),
            name=f"worker-{i}"
        )
        worker.setDaemon(True)
        worker.start()

    # Download the feed(s) and put the enclosure URLs into
    # the queue
    for url in feed_urls:
        response = feedparser.parse(url, agent="fetch_podcasts.py")
        for entry in response["entries"][:5]:
            for enclosure in entry.get("enclosures", []):
                parsed_url = urllib.parse.urlparse(enclosure["url"])
                message(f"queueing {parsed_url.path.rpartition('/')[-1]}")
                enclosure_queue.put(enclosure["url"])

    message("*** main thread waiting")
    enclosure_queue.join()
    message("*** done")


if __name__ == "__main__":
    main()
