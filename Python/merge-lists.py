# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_left = list1
        node_right = list2

        root = ListNode()
        result = root

        while(node_right and node_left):
            val_right = node_right.val
            val_left = node_left.val

            # find min
            if val_right <= val_left:
                result.next = node_right
                node_right = node_right.next
            if val_left < val_right:
                result.next = node_left
                node_left = node_left.next
            result = result.next

        if node_right:
            result.next = node_right
        if node_left:
            result.next = node_left
        
        return root.next