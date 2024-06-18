class MyHashMap:
    def __init__(self):
        self.size = 1000  # Chosen to be large enough to reduce collisions
        self.buckets = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        for idx, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                self.buckets[hash_key][idx] = (key, value)
                return
        self.buckets[hash_key].append((key, value))
        
    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        for k, v in self.buckets[hash_key]:
            if k == key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        for idx, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                del self.buckets[hash_key][idx]
                return
        
    def _hash(self, key: int) -> int:
        return key % self.size
