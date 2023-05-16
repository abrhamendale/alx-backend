#!/usr/bin/env python3
"""
FIFO
"""


class FIFOCache(Basecaching):
    """
    Implements a FIFO cache.
    """

    def __init__(self):
        """
        Initializes a new FIFO instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds to the dictionary.
        """

