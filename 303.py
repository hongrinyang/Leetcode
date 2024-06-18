class NumArray:

    def __init__(self, nums: List[int]):
        self.cumulative_sum = [0]
        current_sum = 0
        for num in nums:
            current_sum += num
            self.cumulative_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]