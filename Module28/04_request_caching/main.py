class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache = {}
        self._order = []

    @property
    def cache(self) -> str:
        if self._order:
            oldest_key = self._order[0]
            return self._cache[oldest_key]
        else:
            return None

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        key, value = new_elem
        if key in self._cache:
            self._order.remove(key)
        elif len(self._cache) >= self._capacity:
            oldest_key = self._order.pop(0)
            del self._cache[oldest_key]
        self._cache[key] = value
        self._order.append(key)


# Пример использования:
cache = LRUCache(3)
cache.cache = ('a', 'apple')
cache.cache = ('b', 'banana')
cache.cache = ('l', 'lemon')
print(cache.cache)
cache.cache = ('c', 'cherry')
print(cache.cache)
