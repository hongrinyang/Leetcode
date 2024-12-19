class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to simplify result handling
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the nodes, defaulting to 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move pointers
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
