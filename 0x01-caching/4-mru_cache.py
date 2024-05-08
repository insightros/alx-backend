#!/usr/bin/python3
"MRU caching"

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    "MRU cache class"

    def __init__(self):
        "Initialize"
        super().__init__()

    def put(self, key, item):
        "Add an item in the cache"
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = list(self.cache_data.keys())[-1]
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item

    def get(self, key):
        "Get an item by key"
        if key is None or key not in self.cache_data:
            return None
        # Update the key to be the most recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
