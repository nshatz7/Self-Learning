# 18. 4Sum

## Problem Statement
Given an array `nums` of `n` integers, return an array of all the **unique quadruplets** `[nums[a], nums[b], nums[c], nums[d]]` such that:
* `0 <= a, b, c, d < n`
* `a`, `b`, `c`, and `d` are distinct.
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

*Note: You may return the answer in any order.*

### Examples
* **Example 1:**
  * **Input:** `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`
  * **Output:** `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`
* **Example 2:**
  * **Input:** `nums = [2, 2, 2, 2, 2]`, `target = 8`
  * **Output:** `[[2, 2, 2, 2]]`

### Constraints
* `1 <= nums.length <= 200`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`

---

## Key Takeaways: Generalizing $k$-Sum Recursion

### Core Concept: Dimensionality Reduction
Sort the array once, then peel off one element at a time via recursion until reaching the **2-Sum base case**, which can be solved in $O(n)$ time using two converging pointers.

### Step-by-Step Procedure

1. **Sort the Array**
   * Run `nums.sort()` first to enable pruning and duplicate skipping.

2. **Define the Recursive Signature**
   * `kSum(start, k, target, nums)`
     * `start`: Lowest index currently available to pick from.
     * `k`: How many numbers still need to be chosen.
     * `target`: Remaining sum required.
     * `nums`: The sorted input array.

3. **Validate Bounds and Prune Branches**
   * *Pruning* means trimming away unnecessary or redundant search branches early:
     * **Length check:** If `start >= len(nums)` or `len(nums) - start < k`, return `[]` *(not enough elements left)*.
     * **Average-value prune:** Compute `avg = target // k`. If `nums[start] > avg` or `nums[-1] < avg`, return `[]` *(even the smallest available elements are too large, or the largest elements in the array are too small to reach `target`)*.

4. **Solve the Base Case (`k == 2`)**
   * Use two converging pointers (`left` and `right`) to find pairs that sum to `target` in $O(n)$ time while skipping duplicate values.

5. **Reduce the Problem Recursively**
   * Loop through `i` (skipping duplicates where `i > start` and `nums[i] == nums[i - 1]`).
   * Call `kSum(i + 1, k - 1, target - nums[i], nums)` to find all valid $(k - 1)$-tuples. *(Recursion continues until `k == 2`, where it hits the base case instead of recursing further).*
   * Prepend/append `nums[i]` to each returned $(k - 1)$-tuple and add it to the final result list.

6. **Trigger the Entry Call**
   * Kick off the recursion from the main function (e.g., `return self.kSum(0, 4, target, nums)`).

---

## Python Syntax Note
To append multiple individual values to a list as their own sub-list (when they aren't already grouped in a list), wrap them in square brackets `[]` inside `.append()`:

```python
numbers = []
# Wrap individual elements in [] to append them as a single sub-list
numbers.append([nums[i], nums[i + 1], nums[i + 2]])
	
