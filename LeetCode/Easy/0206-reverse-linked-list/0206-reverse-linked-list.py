# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  # 1. Save next node
            curr.next = prev       # 2. Reverse pointer
            prev = curr            # 3. Advance prev
            curr = next_temp       # 4. Advance curr
            
        return prev
