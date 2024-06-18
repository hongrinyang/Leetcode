class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollars = 0
        ten_dollars = 0
        
        for bill in bills:
            if bill == 5:
                five_dollars += 5
            elif bill == 10:
                if five_dollars == 0:
                    return False
                five_dollars -= 5
                ten_dollars += 10
            else:  # bill == 20
                if ten_dollars >= 10 and five_dollars >= 5:
                    ten_dollars -= 10
                    five_dollars -= 5
                elif five_dollars >= 15:
                    five_dollars -= 15
                else:
                    return False
        
        return True