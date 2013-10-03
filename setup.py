#!/usr/bin/env python3
from distutils.core import setup

setup(
    name="leftasrain",
    packages=["leftasrain"],
    version="0.0.1",
    description="Listen to/download songs from leftasrain.com from the comfort of your terminal",
    url="https://github.com/naglis/leftasrain",
    license="LICENSE",
    author="Naglis Jonaitis",
    author_email="njonaitis@gmail.com",
    keywords=["script", "leftasrain", "music", "mp3"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Natural Language :: English",
        "License :: Public Domain",
        "Topic :: Utilities"
    ],
    scripts=["leftasrain/leftasrain"],
)
