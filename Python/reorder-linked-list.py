# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # use fast and slow pointers to find middle of linked list
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow
            
        #reverse second half:
        prev = None
        curr = middle.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge
        while prev:
            curr_nxt, prev_nxt = head.next, prev.next
            head.next, prev.next = prev, curr_nxt
            head, prev = curr_nxt, prev_nxt

            # print(head.val)
            # head = head.next
            # if prev:
            #     print(prev.val)
            #     prev = prev.next