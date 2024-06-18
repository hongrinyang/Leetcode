class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append(i)

        if len(diffs) == 2:
            i, j = diffs
            return s[i] == goal[j] and s[j] == goal[i]

        return False