class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        running_sum, partitions = 0, 0
        
        for num in arr:
            running_sum += num
            if running_sum == target:
                partitions += 1
                running_sum = 0  # Reset for the next partition
            
            if partitions == 2 and running_sum == 0:
                # Found two partitions, the third one is implied
                return True
        
        return False
