# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # Sentinel (dummy) node avoids special-casing `head` on the first comparison
        dummy = ListNode(0)
        curr = dummy  # Tail pointer used to append nodes in sorted order

        # Advance whichever list currently has the smaller head value
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # At most one list remains non-empty; since it is already sorted, attach it directly
        curr.next = l1 if l1 else l2

        # dummy.next points to the true head of the merged list
        return dummy.next
