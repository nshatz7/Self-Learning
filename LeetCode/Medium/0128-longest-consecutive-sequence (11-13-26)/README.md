# 128. Longest Consecutive Sequence

## Problem Description
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. 

You must write an algorithm that runs in $O(n)$ time.

### Examples
* **Example 1:**
  * **Input:** `nums = [100, 4, 200, 1, 3, 2]`
  * **Output:** `4`
  * **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is `4`.

* **Example 2:**
  * **Input:** `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
  * **Output:** `9`

* **Example 3:**
  * **Input:** `nums = [1, 0, 1, 2]`
  * **Output:** `3`

### Constraints
* $0 \le \text{nums.length} \le 10^5$
* $-10^9 \le \text{nums}[i] \le 10^9$

---

## Key Takeaways & Concepts Learned

### 1. Identifying Streak Roots ($O(1)$ Set Membership)
* **Approach:** Convert the input array into a `HashSet` to enable $O(1)$ lookups, then iterate through the set.
* **Optimization:** To avoid $O(n^2)$ time complexity, only begin counting a sequence when a number is the **start (root)** of a streak—meaning `num - 1` is **not** in the set.
* **Complexity Trade-off:** Achieves $O(n)$ time complexity, at the cost of $O(n)$ auxiliary space for the hash set.

#### Conceptual Example: Tracking App Login Streaks
Given an unsorted array of days a user logged into an app, find all their consecutive login streaks:

```python
days_set = set(days)  # Turns the list into a set for O(1) lookups
streaks = []          # Empty list to hold all streaks

for day in days_set:
    # Check if 'day' is a streak root (the start of a sequence)
    if (day - 1) not in days_set:
        current_day = day
        
        # Walk forward as long as consecutive days exist
        while (current_day + 1) in days_set:
            current_day += 1
            
        streaks.append(f"Day {day} to Day {current_day}")

return streaks
# Output example: ['Day 2 to Day 5', 'Day 14 to Day 14', 'Day 20 to Day 23']
```

### 2. Why a `set` is Ideal Here (Over a `list` or `dict`)
1. **Deduplication:** Automatically discounts repetitive elements (unlike a `list`), preventing duplicate numbers from messing up the consecutive count or causing redundant iterations.
2. **Simplicity:** You don't need to map or store every streak's length, so a `dictionary` isn't necessary—you only need to track the longest streak as a single integer.

### 3. Useful Python Syntax
* To return the largest value in a list: `max(my_list)`
