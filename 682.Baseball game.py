class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        total_sum = 0
        
        for op in ops:
            if op == '+':
                if len(stack) >= 2:
                    score = stack[-1] + stack[-2]
                    stack.append(score)
                    total_sum += score
            elif op == 'D':
                if stack:
                    score = 2 * stack[-1]
                    stack.append(score)
                    total_sum += score
            elif op == 'C':
                if stack:
                    removed_score = stack.pop()
                    total_sum -= removed_score
            else:
                score = int(op)
                stack.append(score)
                total_sum += score
        
        return total_sum
