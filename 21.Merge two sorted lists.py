class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to form the new list
        dummy = ListNode()
        current = dummy
        
        # Use two pointers to traverse the lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists is not empty, append the rest of the nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts from dummy.next
        return dummy.next

# Helper function to convert list to linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)
print(linkedlist_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 4]
