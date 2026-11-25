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

Divide-and-Conquer Pairwise Merge (O(N log k))
Instead of merging sequentially from left to right (which repeatedly re-traverses already-merged nodes and costs up to O(N * k)), pair up lists and merge two sorted lists at a time across rounds—mirroring the merge stage of Merge Sort:
Round 1: k lists merge in k / 2 pairs. Each pair merges in linear time of its combined elements, so total work across all pairs in the round is O(N) (where N is the total number of nodes across all lists).
Round 2: k / 2 resulting lists merge in k / 4 pairs, again taking O(N) total work across the round.
Subsequent Rounds: Continue halving the active list count (k / 8, k / 16, ...) until a single sorted list remains.
With log2(k) rounds and O(N) work per round, the total time complexity is O(N log k).
