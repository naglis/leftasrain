#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2012-2014 Naglis Jonaitis

"""A script which helps you to listen to/download songs from leftasrain.com
from the comfort of your terminal."""

import json
import queue
import threading
import urllib.parse
import urllib.request

from argparse import ArgumentParser


__license__ = "Public Domain"
__version__ = "0.0.3.1"
__author__ = "Naglis Jonaitis"
__email__ = "njonaitis@gmail.com"

NEXT_TRACK_URL = "http://leftasrain.com/getNextTrack.php?%s"
# this can change over time
SONG_URI_BASE = "http://leftasrain.com/musica/"


def get_song_count():
    """Returns the total number of songs on leftasrain.com"""

    return int(get_song_data(0)[0])


def get_song_data(id):
    """Returns a list of song attributes"""

    params = urllib.parse.urlencode({'currTrackEntry': id, 'shuffle': 'false'})
    result = urllib.request.urlopen(NEXT_TRACK_URL % params)
    return json.loads(result.read().decode("utf-8"))


def worker():
    while True:
        id = queue.get()
        filename = urllib.parse.quote("%s.mp3" % get_song_data(id)[4])
        results[id] = urllib.parse.urljoin(SONG_URI_BASE, filename)
        queue.task_done()


def parse_args():
    parser = ArgumentParser(prog="leftasrain")
    parser.add_argument("-l", "--last", dest="last", metavar="N", type=int,
                        help="download last %(metavar)s songs", default=0)
    parser.add_argument("-t", "--threads", dest="threads", type=int,
                        default=2, metavar="THREADS",
                        help="number of execution THREADS. "
                             "Default: %(default)s")
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + "%s" % __version__)
    return parser.parse_args()


queue = queue.Queue()
results = {}


def main():
    args = parse_args()

    n = get_song_count() + 1
    for i in range(n, args.last == 0 and 1 or n - args.last, -1):
        queue.put(i)

    for i in range(args.threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    # wait for all threads to finish
    queue.join()

    for id in sorted(results.keys(), reverse=True):
        print(results[id])


if __name__ == "__main__":
    main()