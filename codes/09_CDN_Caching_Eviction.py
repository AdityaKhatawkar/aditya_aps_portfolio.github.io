from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # evict LRU
        self.cache[key] = value

# Example: cache video IDs
cache = LRUCache(2)
cache.put("vidA", "VideoA_Data")
cache.put("vidB", "VideoB_Data")
print(cache.get("vidA"))  # Access A
cache.put("vidC", "VideoC_Data")  # Evicts vidB
print(cache.get("vidB"))  # -1 (evicted)
