#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2012-2016 Naglis Jonaitis

"""A script which helps you download songs from leftasrain.com"""

import argparse
import logging
import os

import requests

__version__ = '0.1.0'
LOG = logging.getLogger(__name__)
SONG_INFO_URL = 'http://leftasrain.com/posts/get/{id:}'
STREAM_KEY_URL = 'http://leftasrain.com/streamsong/{id:}'
STREAM_URL = 'http://leftasrain.com/streamsong/{id:}/{key:}'


def get_stream_url(id, s):
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
    }
    url = STREAM_KEY_URL.format(id=id)
    r = s.get(url, headers=headers)
    return STREAM_URL.format(id=id, key=r.text)


def get_song_info(id, s):
    url = SONG_INFO_URL.format(id=id)
    r = s.get(url)
    return r.json()


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    p = argparse.ArgumentParser(prog='leftasrain')
    p.add_argument('song_id', type=int)
    p.add_argument('--version', action='version',
                   version='%%(prog)s %s' % __version__)
    args = p.parse_args()

    s = requests.Session()
    info = get_song_info(args.song_id, s)
    stream_url = get_stream_url(args.song_id, s)

    filename = info.get('song_path', '{id:}.mp3'.format(id=args.song_id))
    if os.path.exists(filename):
        LOG.warn('File: %s exists, skipping.', filename)
    else:
        r = s.get(stream_url)
        with open(filename, 'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    main()
