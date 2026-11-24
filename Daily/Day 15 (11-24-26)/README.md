Day 15 - Self Learning Log

Agenda
LeetCode:
- #76 Minimum Window Sliding
- #239 Sliding Window Maximum
Learning:
- Core focus: Master sliding window with auxiliary demand tracking; monotonic deque optimization.
- Secondary focus: AWS-Dev (course 6)
Production Code:
- Project 1: Backend Development (OpenAPI Documentation)

Conclusion
Completed:
- LeetCode problems with full README's
- 














Core Daily Question: What is sliding window with auxiliary demand tracking and monotonic deque optimization?

Sliding window with auxiliary demand tracking:
Instead of comparing two frequency maps at every step (which costs O(K) time where K is the alphabet size), track unresolved debt in O(1) per pointer movement:

Demand Map (need): Store the required count of each character from t.
Missing Counter (missing): Initialize to len(t). This represents the total number of required characters still owed to make the window valid.
Expand (right pointer):
As s[right] enters the window, check if need[char] > 0. If so, this character pays off part of your debt—decrement missing.
Always decrement need[char]. Characters not in t (or extra duplicates) naturally drop into negative numbers, representing a "surplus".
Contract (left pointer):
Once missing == 0, the window is valid. Shrink from the left to minimize the window length until validity breaks:
Update the minimum window bounds (start, end) if right - left + 1 is a new minimum.
Before removing s[left], increment need[s[left]].
If need[s[left]] > 0, you just evicted a critical character that had zero surplus. Increment missing, which exits the contraction loop and forces right to expand again.

Monotonic Deque Optimization:
If you use a Max-Heap, finding the maximum takes O(1), but removing out-of-bounds elements takes O(log k), yielding O(N log k) overall. A Monotonic Decreasing Deque drops this to O(N) by aggressively pruning useless elements:

The Core Invariant: Imagine two elements in your window, nums[i] and nums[j], where i < j (meaning j arrived later and will stay in the window longer). If nums[j] >= nums[i], then nums[i] can never be the maximum again—it is both smaller and older.
To maintain this invariant, store indices (not values) in a double-ended queue (deque) and enforce three rules at every index i:

Evict the Expired (Front): If the index at dq[0] has fallen outside the current window (dq[0] <= i - k), pop it from the front.
Purge the Weak (Back): While the deque is non-empty and nums[dq[-1]] <= nums[i], pop from the back. nums[i] renders all smaller or equal predecessors obsolete.
Record & Advance: Append i to the back. Because the deque is strictly decreasing from front to back, nums[dq[0]] is guaranteed to be the window maximum once i >= k - 1.



