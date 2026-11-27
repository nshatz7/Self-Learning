# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        # Phase 1: Detect whether a cycle exists and find a meeting node.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                # Phase 2: From L = (m - 1)C + (C - k), walking L steps from head
                # and L steps from the meeting point both land on the cycle entry.
                entry = head
                while entry is not slow:
                    entry = entry.next
                    slow = slow.next

                # Both pointers now reference the exact cycle entry node.
                return entry

        # No cycle found.
        return None

            