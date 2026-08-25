# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        delayed = head
        fast = head

        for i in range(n):
            fast = fast.next

        prev = None
        while fast:
            prev = delayed
            delayed = delayed.next
            fast = fast.next

        # we want to remove this delayed value:
        if not prev:
            return head.next
        if delayed:
            prev.next = delayed.next
        return head