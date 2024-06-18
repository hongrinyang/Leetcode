class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line_width = 0
        line_count = 1
    
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if line_width + char_width > 100:
                line_count += 1
                line_width = char_width
            else:
                line_width += char_width
    
        return [line_count, line_width]
