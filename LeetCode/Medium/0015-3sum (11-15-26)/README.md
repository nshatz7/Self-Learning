# 15. 3Sum

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that $i \neq j$, $i \neq k$, and $j \neq k$, and `nums[i] + nums[j] + nums[k] == 0`.

> **Note:** The solution set must not contain duplicate triplets.

---

### Examples

#### Example 1
* **Input:** `nums = [-1, 0, 1, 2, -1, -4]`
* **Output:** `[[-1, -1, 2], [-1, 0, 1]]`
* **Explanation:**
  * `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`
  * `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`
  * `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`
  * The distinct triplets are `[-1, 0, 1]` and `[-1, -1, 2]`. Notice that the order of the output and the order of the triplets does not matter.

#### Example 2
* **Input:** `nums = [0, 1, 1]`
* **Output:** `[]`
* **Explanation:** The only possible triplet does not sum up to `0`.

#### Example 3
* **Input:** `nums = [0, 0, 0]`
* **Output:** `[[0, 0, 0]]`
* **Explanation:** The only possible triplet sums up to `0`.

---

### Constraints
* $3 \leq \text{nums.length} \leq 3000$
* $-10^5 \leq \text{nums}[i] \leq 10^5$

---

## Key Takeaways & Concepts Learned

### 1. Sort + Two Pointers Pattern
1. **Sort** the array.
2. **Fix** a base index (`i`).
3. **Run two pointers** (`left` and `right`) on the remaining subarray.
4. **Skip duplicates** to ensure unique triplets.

#### Analogy: Stack of Price Tags
Imagine finding two items in a stack of price tags whose prices add up to $\$50$:
1. **Sort the tags:** `[10, 15, 20, 30, 35, 45]`
2. **Place pointers:** `left` starts at `10`, `right` starts at `45`.
3. **Squeeze inward:** Adjust by incrementing `left` (to increase the sum) or decrementing `right` (to decrease the sum) until you hit the target.

---

### 2. The `continue` Statement
The `continue` keyword skips the rest of the current iteration of a loop and moves immediately to the next iteration.

```python
for i in range(len(nums)):
    if i == 0:
        continue  # Skips the rest of the loop body when i == 0 and jumps to i == 1
```
