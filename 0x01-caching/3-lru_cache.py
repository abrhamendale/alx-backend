#!/usr/bin/env python3
"""
LRU
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implements a LRU cache.
    """

    def __init__(self):
        """
        Initializes a new LRU instance.
        """
        self.key_order = []
        self.last_key = []
        super().__init__()

    def put(self, key, item):
        """
        Adds to the dictionary.
        """
        if key not in self.key_order and len(self.cache_data) >= self.MAX_ITEMS:
            for i in range(len(self.last_key) - 1, 0, -1):
                if self.last_key[i] == 1:
                    self.last_key[i] = 0
                    del self.cache_data[self.key_order[i]]
                    print("DISCARD:", self.key_order[i])
                    break

        if key and item:
            if self.cache_data is None:
                self.lpush = key
            self.cache_data[key] = item
            self.key_order.append(key)
            self.last_key.append(1)

    def get(self, key):
        """
        Retrieves from the cache
        """
        if key and item:
            return (self.cache_data[key])
