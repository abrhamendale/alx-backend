#!/usr/bin/env python3
"""
FIFO cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a Basic dictionary.
    """

    def __init__(self):
        """
        Initializes a new BasicCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an element to the dictionary..
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an element from the dictionary.
        """
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
