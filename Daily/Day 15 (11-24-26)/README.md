Core Daily Question: What is sliding window with auxiliary demand tracking and monotonic deque optimization?

Sliding window with auxiliary demand tracking:


Monotonic Deque Optimization:
If you use a Max-Heap, finding the maximum takes O(1), but removing out-of-bounds elements takes O(log k), yielding O(N log k) overall. A Monotonic Decreasing Deque drops this to O(N) by aggressively pruning useless elements:

The Core Invariant: Imagine two elements in your window, nums[i] and nums[j], where i < j (meaning j arrived later and will stay in the window longer). If nums[j] >= nums[i], then nums[i] can never be the maximum again—it is both smaller and older.
To maintain this invariant, store indices (not values) in a double-ended queue (deque) and enforce three rules at every index i:

Evict the Expired (Front): If the index at dq[0] has fallen outside the current window (dq[0] <= i - k), pop it from the front.
Purge the Weak (Back): While the deque is non-empty and nums[dq[-1]] <= nums[i], pop from the back. nums[i] renders all smaller or equal predecessors obsolete.
Record & Advance: Append i to the back. Because the deque is strictly decreasing from front to back, nums[dq[0]] is guaranteed to be the window maximum once i >= k - 1.



