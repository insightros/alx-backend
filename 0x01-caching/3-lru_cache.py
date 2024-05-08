#!/usr/bin/python3
"LRU caching"

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    "LRU cache class"

    def __init__(self):
        "Initialize"
        super().__init__()
        self.queue = []

    def put(self, key, item):
        "Add an item in the cache"
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            elif key in self.cache_data:
                self.queue.remove(key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        "Get an item by key"
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
