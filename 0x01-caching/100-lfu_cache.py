#!/usr/bin/env python3
"""
LFU cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Implements a LFU cache.
    """

    def __init__(self):
        """
        Initializes a new LFU instance.
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
                for i in range(0, len(self.last_key)):
                    if self.last_key[i] == min(self.last_key):
                        del self.cache_data[self.key_order[i]]
                        print("DISCARD:", self.key_order[i])
                        del self.key_order[i]
                        del self.last_key[i]
                        break

        if key and item:
            self.cache_data[key] = item
            if key not in self.key_order:
                self.key_order.append(key)
                self.last_key.append(1)
            else:
                b = self.key_order.index(key)
                self.last_key[b] = self.last_key[b] + 1

    def get(self, key):
        """
        Retrieves from the cache
        """
        if key and key in self.cache_data.keys():
            a = self.key_order.index(key)
            self.last_key[a] = self.last_key[a] + 1
            return (self.cache_data[key])
