class RLEIterator:
    def __init__(self, encoding):
        # Initialize the encoded array and the current index
        self.encoding = encoding
        self.index = 0
    
    def next(self, n):
        # Traverse the encoded array to find the next valid element
        while self.index < len(self.encoding):
            count = self.encoding[self.index]
            value = self.encoding[self.index + 1]
            
            if count >= n:
                # If the current count is enough to fulfill the request
                self.encoding[self.index] -= n  # Decrease the count
                return value
            else:
                # If the current count is less than n, exhaust it and move to the next pair
                n -= count
                self.index += 2
        
        # If there are no elements left to exhaust, return -1
        return -1
