# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
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

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Handle empty input list (`lists == []`)
        if not lists:
            return None

        def merge_range(left: int, right: int) -> ListNode | None:
            # Base case: single list in range needs no merging
            if left == right:
                return lists[left]

            # Split range into two halves and merge each half first
            mid = left + (right - left) // 2
            l1 = merge_range(left, mid)
            l2 = merge_range(mid + 1, right)

            # Reuse the two-pointer helper via `self` on the two resulting lists
            return self.mergeTwoLists(l1, l2)

        return merge_range(0, len(lists) - 1)


"""
Time complexity:
- Merging two lists with length m and n takes O(m + n).
- In mergeKLists, we recursively merge ranges in a divide-and-conquer fashion, resulting in O(k log k) merge steps over the total N nodes, giving overall time complexity O(N log k) where N is the total number of nodes across all lists and k is the number of lists.
Space complexity:
- The iterative mergeTwoLists uses O(1) extra space besides the new links (constant extra pointers).
- The recursive approach for mergeKLists uses stack space proportional to the recursion depth, which is O(log k). The total auxiliary space is O(log k); the resulting merged list uses existing nodes, so no extra node allocations are required.
"""
