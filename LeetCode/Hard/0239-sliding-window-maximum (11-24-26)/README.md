# 239. Sliding Window Maximum

## Problem Statement

Given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the **max sliding window**.

### Examples

#### Example 1
* **Input:** `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`
* **Output:** `[3, 3, 5, 5, 6, 7]`
* **Explanation:**

| Window Position | Max |
| :--- | :---: |
| `[1  3  -1] -3  5  3  6  7` | **3** |
| ` 1 [3  -1  -3] 5  3  6  7` | **3** |
| ` 1  3 [-1  -3  5] 3  6  7` | **5** |
| ` 1  3  -1 [-3  5  3] 6  7` | **5** |
| ` 1  3  -1  -3 [5  3  6] 7` | **6** |
| ` 1  3  -1  -3  5 [3  6  7]` | **7** |

#### Example 2
* **Input:** `nums = [1]`, `k = 1`
* **Output:** `[1]`

### Constraints
* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `1 <= k <= nums.length`

---

## Key Concept: Monotonic Deque Optimization ("Survival of the Fittest & Youngest")

If you use a Max-Heap, finding the maximum takes `O(1)`, but removing out-of-bounds elements takes `O(log k)`, yielding `O(N log k)` overall. A **Monotonic Decreasing Deque** drops this to `O(N)` by aggressively pruning useless elements:

* **The Core Invariant:** Imagine two elements in your window, `nums[i]` and `nums[j]`, where `i < j` (meaning `j` arrived later and will stay in the window longer). If `nums[j] >= nums[i]`, then `nums[i]` can **never** be the maximum again—it is both smaller and older.

To maintain this invariant, store **indices** (not values) in a double-ended queue (`deque`) and enforce three rules at every index `i`:

1. **Evict the Expired (Front):** If the index at `dq[0]` has fallen outside the current window (`dq[0] <= i - k`), pop it from the front.
2. **Purge the Weak (Back):** While the deque is non-empty and `nums[dq[-1]] <= nums[i]`, pop from the back. `nums[i]` renders all smaller or equal predecessors obsolete.
3. **Record & Advance:** Append `i` to the back. Because the deque is strictly decreasing from front to back, `nums[dq[0]]` is guaranteed to be the window maximum once `i >= k - 1`.

