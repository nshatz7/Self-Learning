# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


    def hasCycle(self, head: ListNode | None) -> bool:
        # Start both pointers at the head of the linked list.
        slow = head
        fast = head

        # Stop if fast reaches the end (None) or cannot advance two steps.
        while fast is not None and fast.next is not None:
            # Tortoise moves 1 step; hare moves 2 steps.
            slow = slow.next
            fast = fast.next.next

            # Inside a cycle, fast closes the gap by 1 node per step until they collide.
            if slow is fast:
                return True

        # Reached the end without meeting, so no cycle exists.
        return False

            