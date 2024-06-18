class MyHashSet:
    def __init__(self):
        self.size = 1000  # Chosen to be large enough to reduce collisions
        self.buckets = [[] for _ in range(self.size)]
        
    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        if not self.contains(key):
            self.buckets[hash_key].append(key)
        
    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        if self.contains(key):
            self.buckets[hash_key].remove(key)
        
    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        return key in self.buckets[hash_key]
    
    def _hash(self, key: int) -> int:
        return key % self.size
