# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def merge(self, list1, list2):
        # let's merge !!
        # print(list1)
        # print(list2)
        # print()
        result = ListNode()
        head = result

        while list1 and list2:
            # find the min:
            val1 = list1.val
            val2 = list2.val
            if val1 < val2:
                result.next = list1
                list1 = list1.next
            elif val2 <= val1:
                result.next = list2
                list2 = list2.next
            result = result.next

        if list1:
            result.next = list1

        if list2:
            result.next = list2

        return head.next

    def merge_sort(self, head: ListNode) -> ListNode:
        # base case
        if not head.next:
            return head

        # first find middle
        # then create two different linked lists (first and second half):
        # we will use the slow/ fast approach
        slow = head
        fast = head

        list1 = head
        prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # middle is slow
        prev.next = None
        list2 = slow

        list1 = self.merge_sort(list1)
        list2 = self.merge_sort(list2)

        return self.merge(list1, list2)
        # now we have our two lists

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        result = self.merge_sort(head)
        # let's try mergesort somehow
        return result