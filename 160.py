class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLengthAndTail(head):
            length = 0
            tail = None
            while head:
                length += 1
                tail = head
                head = head.next
            return length, tail
        
        lenA, tailA = getLengthAndTail(headA)
        lenB, tailB = getLengthAndTail(headB)
        
        if tailA is not tailB:
            return None
        
        longer, shorter = (headA, headB) if lenA > lenB else (headB, headA)
        for _ in range(abs(lenA - lenB)):
            longer = longer.next
        
        while longer and shorter:
            if longer is shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        
        return None