# 56. Merge Intervals

## Problem Statement
Given an array of `intervals` where $\text{intervals}[i] = [\text{start}_i, \text{end}_i]$, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Examples

**Example 1:**
* **Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
* **Output:** `[[1,6],[8,10],[15,18]]`
* **Explanation:** Since intervals `[1,3]` and `[2,6]` overlap, merge them into `[1,6]`.

**Example 2:**
* **Input:** `intervals = [[1,4],[4,5]]`
* **Output:** `[[1,5]]`
* **Explanation:** Intervals `[1,4]` and `[4,5]` are considered overlapping.

**Example 3:**
* **Input:** `intervals = [[4,7],[1,4]]`
* **Output:** `[[1,7]]`
* **Explanation:** Intervals `[1,4]` and `[4,7]` are considered overlapping.

### Constraints
* $1 \le \text{intervals.length} \le 10^4$
* $\text{intervals}[i].\text{length} == 2$
* $0 \le \text{start}_i \le \text{end}_i \le 10^4$

---

## Key Takeaways & Lessons Learned

### Interval Boundary Comparison
When checking if two intervals overlap, writing out 6 `if/else` statements is messy and bug-prone. Instead, **sort by the start time first**. This immediately eliminates two edge cases and guarantees that for any two consecutive intervals $A$ and $B$, $A.\text{start} \le B.\text{start}$.

### The Two-Question Decision Tree
Once $A.\text{start} \le B.\text{start}$ is guaranteed, you only need to perform two simple boundary checks:

1. **Do they overlap?** *(Compare $A.\text{end}$ vs. $B.\text{start}$)*
   * **Case 1 ($A.\text{end} < B.\text{start}$):** There is a gap; they **do not** overlap.
   * **Case 2 ($A.\text{end} \ge B.\text{start}$):** They **do** overlap (touching boundaries like `[1,4]` and `[4,5]` count as overlapping).

2. **If they merge, what is the new merged interval?**
   * **New Start:** Always $\min(A.\text{start}, B.\text{start})$. *(Since the array is already sorted, this is simply $A.\text{start}$).*
   * **New End:** Always $\max(A.\text{end}, B.\text{end})$. *(Using $\max()$ automatically handles both partial overlaps and full containment without needing separate logic).*
