# 643. Maximum Average Subarray I

## Problem Statement
Given an integer array `nums` consisting of $n$ elements, and an integer $k$, find a contiguous subarray whose **length is equal to $k$** that has the maximum average value and return this value. Any answer with a calculation error less than $10^{-5}$ will be accepted.

### Examples
**Example 1:**
* **Input:** `nums = [1, 12, -5, -6, 50, 3]`, `k = 4`
* **Output:** `12.75000`
* **Explanation:** Maximum average is $(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75$

**Example 2:**
* **Input:** `nums = [5]`, `k = 1`
* **Output:** `5.00000`

### Constraints
* $n == \text{nums.length}$
* $1 \le k \le n \le 10^5$
* $-10^4 \le \text{nums}[i] \le 10^4$

---

## Key Takeaways & Approach

### Fixed-Window Running Sum Template
* **Complexity:** $O(n)$ time | $O(1)$ space
* **Why use it:** Recalculating `sum(nums[i:i+k])` on every step takes $O(n \cdot k)$ time and triggers a **Time Limit Exceeded (TLE)** error. A sliding window updates the sum in $O(1)$ time per step.

```python
# 1. Compute the first window's sum once (indices 0 to k - 1)
window_sum = sum(arr[:k])

# 2. Record the result for that initial window
# [Problem-specific logic goes here]

# 3. Slide the window one step at a time from index k to n - 1
for i in range(k, len(arr)):
    # Add incoming right element (arr[i])
    # Subtract outgoing left element (arr[i - k])
    window_sum += arr[i] - arr[i - k]
    
    # Update the result for the new window
    # [Problem-specific logic goes here]
```

### Problem-Specific Insights
1. **Why `i - k` works:** When the pointer is at index $i$, the current window of length $k$ covers indices $[i - k + 1 \dots i]$. The element that just fell off the left edge was at index $i - k$.
2. **Handling Negative Numbers:** 
   * **Never** initialize `max_sum = 0` (if all numbers are negative, this will erroneously return `0.0` instead of the actual negative maximum).
   * **Always** set `max_sum = window_sum` right after building the first window.
3. **Optimize Division:** 
   * Since $k$ is positive and fixed, the window with the largest sum automatically has the largest average.
   * Track integer sums inside the loop and perform `return max_sum / k` once at the very end to avoid unnecessary floating-point division on every iteration.

