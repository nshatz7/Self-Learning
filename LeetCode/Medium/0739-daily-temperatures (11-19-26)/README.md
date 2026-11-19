# 739. Daily Temperatures

## Problem Statement

Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the $i^{\text{th}}$ day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

---

### Examples

**Example 1:**
```text
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**
```text
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```text
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

### Constraints
* $1 \le \text{temperatures.length} \le 10^5$
* $30 \le \text{temperatures}[i] \le 100$

---

## Key Takeaways

### 1. Monotonic Decreasing Stack (For Daily Temperatures)
To avoid an $O(n^2)$ nested loop checking future days for every temperature, use a **monotonic decreasing stack** that stores indices of unresolved days:
* Iterate through the array of temperatures.
* While the stack is non-empty and the current temperature is **strictly greater** than the temperature at the index on top of the stack, we have found the next warmer day for that previous index.
* Pop the previous index `prev_idx` and record the wait time: `answer[prev_idx] = current_idx - prev_idx`.
* Push `current_idx` onto the stack to await its own warmer day.

#### Implementation (Python)
```python
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices of temperatures in decreasing order

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return answer
```

#### Complexity Analysis
* **Time Complexity:** $O(n)$ — Although there is a `while` loop inside the `for` loop, each index is pushed onto the stack once and popped at most once.
* **Space Complexity:** $O(n)$ — In the worst case (strictly decreasing temperatures), all $n$ indices remain in the stack.

---

### 2. Side Note: Space-Optimized Two-Stack Approach (Revisiting Min Stack)
Instead of duplicating the minimum value on every push (like in tuple-based auxiliary state tracking), you can maintain a separate `min_stack` that only pushes a new value when `val <= min_stack[-1]`:
* **Push:** Always push to `main_stack`. Only push to `min_stack` if `min_stack` is empty or `val <= min_stack[-1]`.
* **Pop:** Pop from `main_stack`. If the popped value equals `min_stack[-1]`, pop from `min_stack` as well.
* **Benefit:** Saves auxiliary memory when duplicates or non-minimum elements are frequently pushed, while preserving $O(1)$ time complexity.
