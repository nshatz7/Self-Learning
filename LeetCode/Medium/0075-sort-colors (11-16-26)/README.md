# 75. Sort Colors

## Problem Statement

Given an array `nums` with $n$ objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function. Do not return anything; just modify `nums` in-place.

### Examples

**Example 1:**
* **Input:** `nums = [2,0,2,1,1,0]`
* **Output:** `[0,0,1,1,2,2]`
* **Explanation:** The array has two `0`s, two `1`s, and two `2`s. Sorting them in-place places all `0`s first, then all `1`s, then all `2`s.

**Example 2:**
* **Input:** `nums = [2,0,1]`
* **Output:** `[0,1,2]`
* **Explanation:** The array has one each of `0`, `1`, and `2`, arranged in-place in the order `0`, `1`, `2`.

### Constraints
* $n == \text{nums.length}$
* $1 \le n \le 300$
* $\text{nums}[i]$ is either `0`, `1`, or `2`.

---

## Key Concepts Learned

### Dutch National Flag Algorithm
The optimal approach uses the **Dutch National Flag algorithm**, which sorts the array in a single pass ($O(n)$ time, $O(1)$ space) by maintaining three pointer boundaries (`low`, `mid`, and `high`) that divide the array into four distinct regions at all times:

| Region | Range | Contents |
| :--- | :--- | :--- |
| **1. Confirmed 0s** | `[0 ... low - 1]` | All `0`s (Red) |
| **2. Confirmed 1s** | `[low ... mid - 1]` | All `1`s (White) |
| **3. Unknown Zone** | `[mid ... high]` | Unsorted / active window (`???`) |
| **4. Confirmed 2s** | `[high + 1 ... n - 1]` | All `2`s (Blue) |

### Step-by-Step Procedure

1. **Initialize Pointers:**
   * `low = 0`
   * `mid = 0`
   * `high = len(nums) - 1`
2. **Loop Condition:**
   * Run `while mid <= high:`. Once `mid` crosses `high`, the unknown zone vanishes and the entire array is sorted.
3. **Shrink the Unknown Zone:**
   * **Case `nums[mid] == 0`:**
     * Swap `nums[low]` and `nums[mid]`.
     * Increment **both** `low` and `mid` by `1`.
   * **Case `nums[mid] == 1`:**
     * Increment `mid` by `1`.
   * **Case `nums[mid] == 2` (`else`):**
     * Swap `nums[high]` and `nums[mid]`.
     * Decrement **only** `high` by `1` *(do not increment `mid`, because the newly swapped element from `high` hasn't been evaluated yet)*.

### Implementation (Python)

```python
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
```

---

## Python Syntax Takeaway

* **Invalid:** `variable1, variable2 += 1`
* **Why:** Raises a `SyntaxError` because augmented assignment operators (`+=`, `-=`) can only target a single variable at a time, not a tuple.
* **Fix:** Increment them on separate lines (`low += 1` and `mid += 1`).
















