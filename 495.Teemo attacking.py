class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
    
        total_poisoned_time = 0
        prev_end_time = timeSeries[0] - 1  # Initialize with an invalid time

        for time in timeSeries:
            end_time = time + duration - 1
            total_poisoned_time += duration
        
            if time <= prev_end_time:
                total_poisoned_time -= (prev_end_time - time + 1)
        
            prev_end_time = end_time
    
        return total_poisoned_time
