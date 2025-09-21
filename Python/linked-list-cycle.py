# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        while head:
            visited.append(head)
            next = head.next
            if next in visited:
                return True
            head = next

        return False