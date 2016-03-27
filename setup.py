#!/usr/bin/env python3
from setuptools import setup

version='0.1.0'

setup(
    name='leftasrain',
    version=version,
    description='Listen to/download songs from leftasrain.com from the comfort of your terminal',
    url='https://github.com/naglis/leftasrain',
    author='Naglis Jonaitis',
    author_email='naglis@mailbox.org',
    keywords=['script', 'leftasrain', 'music', 'mp3'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: Public Domain',
        'Topic :: Utilities'
    ],
    install_requires=['requests'],
    py_modules=['leftasrain'],
    entry_points={'console_scripts': [ 'leftasrain = leftasrain:main' ]},
)
