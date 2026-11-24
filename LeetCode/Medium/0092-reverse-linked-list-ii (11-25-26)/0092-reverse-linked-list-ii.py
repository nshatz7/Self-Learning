class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Dummy node eliminates edge cases when left == 1
        dummy = ListNode(0, head)
        before_sublist = dummy

        # Phase 1: Move to the node right before `left`
        for _ in range(left - 1):
            before_sublist = before_sublist.next

        # Save the first node of the sublist (it becomes the tail after reversal)
        sublist_tail = before_sublist.next

        # Phase 2: Standard 3-pointer reversal for (right - left + 1) nodes
        prev = None
        curr = sublist_tail
        for _ in range(right - left + 1):
            next_temp = curr.next  # 1. Save next node
            curr.next = prev       # 2. Reverse pointer
            prev = curr            # 3. Advance prev
            curr = next_temp       # 4. Advance curr

        # Phase 3: Reconnect boundaries
        before_sublist.next = prev  # Connect node before `left` to new sublist head (`right`)
        sublist_tail.next = curr    # Connect new sublist tail (`left`) to node after `right`

        return dummy.next


"""
Time complexity: 
    - O(n), where n is the number of nodes in the list. Each node is visited a constant number of times (once to reach the left boundary and once during the reversal).
Space complexity: 
    - O(1) auxiliary space. The algorithm uses a fixed number of pointers (dummy, before_sublist, sublist_tail, prev, curr, next_temp) regardless of list size. No extra data structures are allocated.
"""
