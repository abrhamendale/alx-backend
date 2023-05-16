#!/usr/bin/env python3
"""
LIFO cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements a LIFO cache.
    """

    def __init__(self):
        """
        Initializes a new LIFO instance.
        """
        self.key_order = []
        self.last_key = []
        super().__init__()

    def put(self, key, item):
        """
        Adds to the dictionary.
        """
        if key not in self.key_order:
            if len(self.cache_data) >= self.MAX_ITEMS:
                for i in range(len(self.last_key) - 1, 0, -1):
                    if self.last_key[i] == 1:
                        self.last_key[i] = 0
                        del self.cache_data[self.key_order[i]]
                        print("DISCARD:", self.key_order[i])
                        self.key_order.remove(self.key_order[i])
                        del self.last_key[i]
                        break

        if key and item:
            if self.cache_data is None:
                self.lpush = key
            self.cache_data[key] = item
            """if key not in self.key_order:"""
            self.key_order.append(key)
            self.last_key.append(1)

    def get(self, key):
        """
        Retrieves from the cache
        """
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
