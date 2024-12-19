class PeekingIterator:
    def __init__(self, iterator):
        # Initialize the iterator and cache the next element
        self.iterator = iterator
        self.cache = None
        if self.iterator.hasNext():
            self.cache = self.iterator.next()

    def peek(self):
        # Return the cached element without moving the iterator
        return self.cache

    def next(self):
        # Return the cached element and move the iterator to the next element
        next_element = self.cache
        if self.iterator.hasNext():
            self.cache = self.iterator.next()
        else:
            self.cache = None  # No more elements, reset cache to None
        return next_element

    def hasNext(self):
        # If there's a cached element, it means there's a next element
        return self.cache is not None
