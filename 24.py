class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node to simplify the swapping logic
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Traverse the list in pairs
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Swapping the nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev two nodes ahead for the next pair
            prev = first
        
        # Return the new head of the list
        return dummy.next
