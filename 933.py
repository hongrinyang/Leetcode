class RecentCounter:
    def __init__(self):
        # Initialize an empty queue to store timestamps
        self.queue = []
    
    def ping(self, t: int) -> int:
        # Add the new timestamp to the queue
        self.queue.append(t)
        
        # Remove timestamps that are outside the 3000ms window
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        
        # Return the number of timestamps in the current 3000ms window
        return len(self.queue)
