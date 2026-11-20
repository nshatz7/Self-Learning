# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

## Problem Statement
Given an array of integers `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size `k` and average greater than or equal to `threshold`.

### Examples
**Example 1:**
* **Input:** `arr = [2, 2, 2, 2, 5, 5, 5, 8]`, `k = 3`, `threshold = 4`
* **Output:** `3`
* **Explanation:** Sub-arrays `[2, 5, 5]`, `[5, 5, 5]`, and `[5, 5, 8]` have averages `4`, `5`, and `6` respectively. All other sub-arrays of size `3` have averages less than `4` (the threshold).

**Example 2:**
* **Input:** `arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]`, `k = 3`, `threshold = 5`
* **Output:** `6`
* **Explanation:** The first `6` sub-arrays of size `3` have averages greater than `5`. Note that averages are not integers.

### Constraints
* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^4`
* `1 <= k <= arr.length`
* `0 <= threshold <= 10^4`

---

## Key Takeaways & Approach

### Fixed-Window Running Sum Pattern
* **Complexity:** `O(n)` time | `O(1)` space
* **Approach:** Uses the standard fixed-size sliding window template, maintaining a running sum in `O(1)` time per step rather than recomputing the sum from scratch.

### Problem-Specific Insights
1. **Turn Division into Multiplication:**
   * Checking `window_sum / k >= threshold` inside the loop requires floating-point division on every iteration and risks floating-point precision issues.
   * Since `k > 0`, rearrange the inequality before the loop starts:
     `window_sum / k >= threshold`  -->  `window_sum >= threshold * k`
   * Precompute `target = threshold * k` once, then compare integers directly inside the loop.
2. **Score the Initial Window Before the Loop:**
   * Because the `for` loop starts at index `k` (which represents the *second* window position), you must check whether the first window (`arr[:k]`) meets the target inequality **before** entering the loop. Skipping this will result in an off-by-one error on `count`.
