class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Sort the list
        strs.sort()
        
        # The common prefix of the first and last strings in the sorted list
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]

# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
