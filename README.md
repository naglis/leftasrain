# leftasrain
Listen to/download songs from [leftasrain.com][lar] from the comfort of your
terminal.

## Requirements
- Python 3.3

## Installation
```bash
$ pip install leftasrain
```

## Usage
To use it, simply execute:
```bash
$ leftasrain
```

This will output links to all songs on [leftasrain][lar]. Not much use, heh?

Let's play the latest 100 songs:
```bash
$ leftasrain -l 100 | mplayer -playlist -
```

Shuffle?
```bash
$ leftasrain -l 100 | mplayer -shuffle -playlist -
```

Listen to [leftasrain][lar] in `mpd`?
```bash
$ leftasrain -t 6 > ~/.mpd/playlists/leftasrain.m3u
```
Note: your mpd playlist directory may be different. Please refer to your mpd
configuration.

Ok, what about downloading?
```bash
$ leftasrain | wget -nc -i -
```

To speed things up, several threads can be used:
```bash
$ leftasrain -l 100 -t 6
```

The default number of threads is `2`.

## Disclaimer
I take no responsibility for any legal issues that may arise from you
listening to or downloading songs from leftasrain.com.

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.


[lar]: http://leftasrain.com/
