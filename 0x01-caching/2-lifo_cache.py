#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a FIFO caching system"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """add an item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """get an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
