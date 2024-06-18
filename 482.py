class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()

        length = len(s)

        first_group_length = length % k
        if first_group_length == 0:
            first_group_length = k

        result = s[:first_group_length]

        for i in range(first_group_length, length, k):
            result += '-' + s[i:i+k]
        
        return result
