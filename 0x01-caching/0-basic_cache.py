#!/usr/bin/env python3
"basic chaching"
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    "represents object"
    def put(self, key, item):
        "adds key"
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        "retrieves key"
        return self.cache_data.get(key, None)
