#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a caching system"""
    def put(self, key, item):
        """Add an item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
