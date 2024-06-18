class Solution:
    def findRelativeRanks(self, score):
        indexed_scores = [(score[i], i) for i in range(len(score))]
        
        indexed_scores.sort(reverse=True, key=lambda x: x[0])
        
        n = len(score)
        answer = [""] * n
        
        for i in range(n):
            if i == 0:
                answer[indexed_scores[i][1]] = "Gold Medal"
            elif i == 1:
                answer[indexed_scores[i][1]] = "Silver Medal"
            elif i == 2:
                answer[indexed_scores[i][1]] = "Bronze Medal"
            else:
                answer[indexed_scores[i][1]] = str(i + 1)
        
        return answer
