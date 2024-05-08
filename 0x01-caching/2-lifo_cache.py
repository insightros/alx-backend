#!/usr/bin/python3
"LIFO caching"

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    "LIFO cache class"

    def __init__(self):
        "Initialize"
        super().__init__()

    def put(self, key, item):
        "Add an item in the cache"
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item (LIFO)
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        "Get an item by key"
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
