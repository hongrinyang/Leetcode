class Solution:

    memo = {0: [""], 1: ["()"]}

    def generateParenthesis(self, n: int) -> List[str]:
        if n in Solution.memo:
            return Solution.memo[n]

        
        out = []
        for n_inside_parenthesis in range(n):
            for s in self.generateParenthesis(n_inside_parenthesis):
                for s_right in self.generateParenthesis(n-1-n_inside_parenthesis):
                    out.append("(" + s + ")" + s_right )
        
        Solution.memo[n] = out
        return out