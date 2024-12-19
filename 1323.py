class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)  # Convert the number to a string
        
        # Find the first '6' and change it to '9'
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str = num_str[:i] + '9' + num_str[i+1:]  # Change '6' to '9'
                break  # Only change the first '6'
        
        return int(num_str)  # Convert the string back to an integer
