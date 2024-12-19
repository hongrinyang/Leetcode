class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # to store previous string and multipliers
        current_string = ""  # to build the current string
        current_num = 0  # to store the current multiplier
        
        for char in s:
            if char.isdigit():
                # If the character is a digit, build the number
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and multiplier onto the stack
                stack.append((current_string, current_num))
                current_string, current_num = "", 0  # reset current string and multiplier
            elif char == ']':
                # Pop from the stack and repeat the current string
                prev_string, repeat_count = stack.pop()
                current_string = prev_string + current_string * repeat_count
            else:
                # If the character is a letter, add it to the current string
                current_string += char
        
        return current_string

# Example Usage
solution = Solution()

# Test case 1
s = "3[a]2[bc]"
print(solution.decodeString(s))  # Output: "aaabcbc"

# Test case 2
s = "3[a2[c]]"
print(solution.decodeString(s))  # Output: "accaccacc"

# Test case 3
s = "2[abc]3[cd]ef"
print(solution.decodeString(s))  # Output: "abcabccdcdcdef"
