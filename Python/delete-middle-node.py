# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        # find middle
        slow = head
        fast = head
        prev = None
        nxt = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            nxt = slow.next
        
        curr = head
        while curr:
            if curr == prev:
                curr.next = nxt
                break
            curr = curr.next

        return head