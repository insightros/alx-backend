#!/usr/bin/python3
""" LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.freq = {}
        self.key_freq = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [k for k, v in self.freq.items() if v == min_freq]
                if len(least_freq_keys) == 1:
                    discarded_key = least_freq_keys[0]
                else:
                    # Use LRU to discard the least recently used item
                    discarded_key = min(self.key_freq, key=self.key_freq.get)
                del self.cache_data[discarded_key]
                del self.freq[discarded_key]
                del self.key_freq[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.key_freq[key] = 0
            self.freq[key] = 0

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.key_freq[key] += 1
        self.freq[key] += 1
        return self.cache_data[key]
