class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Base case: if the list is empty or k = 1, no reversal needed
        if not head or k == 1:
            return head
        
        # Function to reverse k nodes
        def reverse_linked_list(start, k):
            prev, cur = None, start
            while k:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                k -= 1
            return prev
        
        # Dummy node to handle edge case when reversing the first group
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while head:
            # Check if there are enough nodes to reverse
            tail = group_prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            
            # Identify the start and end of the group
            group_start = group_prev.next
            group_end = tail.next
            
            # Reverse the group
            group_prev.next = reverse_linked_list(group_start, k)
            
            # Connect the reversed group to the next part of the list
            group_start.next = group_end
            group_prev = group_start
            head = group_end
        
        return dummy.next
