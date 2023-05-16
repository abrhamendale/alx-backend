#!/usr/bin/env python3
"""
LRU cache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implements a LRU cache.
    """

    def __init__(self):
        """
        Initializes a new LRU cache instance.
        """
        self.lru_order = []
        self.lru_key = []
        self.lru_bit = 0
        self.inc = 1
        super().__init__()

    def put(self, key, item):
        """
        Adds to the dictionary.
        """
        if key not in self.lru_order:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.lru_bit = self.lru_key.index(min(self.lru_key))
                del self.cache_data[self.lru_order[self.lru_bit]]
                print("DISCARD:", self.lru_order[self.lru_bit])
                self.lru_order.remove(self.lru_order[self.lru_bit])
                self.lru_key.remove(self.lru_key[self.lru_bit])

        if key and item:
            self.cache_data[key] = item
            if key not in self.lru_order:
                self.lru_order.append(key)
                self.lru_key.append(self.inc)
                self.inc = self.inc + 1
            else:
                self.lru_key[self.lru_order.index(key)] = self.inc
                self.inc = self.inc + 1

    def get(self, key):
        """
        Retrieves from the cache
        """
        if key and key in self.cache_data:
            for i in range(0, len(self.lru_order)):
                if self.lru_order[i] == key:
                    self.lru_key[i] = self.inc
                    self.inc = self.inc + 1
            return (self.cache_data[key])
        else:
            return (None)
