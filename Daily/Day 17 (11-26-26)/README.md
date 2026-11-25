Core daily question: What is Sentinel/dummy head nodes and scaling from 2 pointers to a priority queue (O(Nlogk)) or divide-and-conquer merge?

How the Sentinel Pattern Works
Allocate a placeholder node (dummy = ListNode(0)) and set a builder pointer curr = dummy.
While both list1 and list2 are non-empty:
Compare list1.val and list2.val.
Attach the smaller node to curr.next, advance that list's pointer forward, and advance curr = curr.next.
Once one list is exhausted, attach the remaining non-empty list directly to curr.next (curr.next = list1 or list2).
Return dummy.next.
Why It Matters
Uniform Loop Logic: Every step follows the exact same attachment and advancement pattern—no special cases for the first element or empty lists.
Fewer Pointer Bugs: Eliminates awkward head initialization checks and reduces null-pointer or off-by-one mistakes.
