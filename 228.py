class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        def format_range(start, end):
            if start == end:
                return str(start)
            else:
                return f"{start}->{end}"

        ranges = []
        start = end = nums[0]
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                ranges.append(format_range(start, end))
                start = end = num

        ranges.append(format_range(start, end))
        return ranges
