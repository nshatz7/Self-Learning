# Contains Duplicate

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example
```text
Input: nums = [1, 2, 3, 1]
Output: true
```
**Explanation:** The element `1` occurs at indices `0` and `3`.

---

## Key Takeaways & What I Learned

### 1. Avoiding Nested Loops (\(O(n^2)\))
* Using two nested loops results in a quadratic time complexity of **`O(n^2)`**, which becomes too slow for large datasets.
* **The Fix:** Use Python data structures that allow for **`O(1)`** (constant time) existence checks:
  * **`set`:** Checks if an item exists (used in my solution).
  * **`dict`:** Looks up a value via a key.

### 2. Understanding Loops & Sets in Python
* **Linear Complexity:** Adding a single `for` loop makes a function **`O(n)`** linear. Loops are often necessary when analyzing specific values, though here we only care about duplication rather than the values themselves.
* **Automatic Deduplication:** Converting a list with duplicates into a `set` automatically strips out duplicate items, leaving only unique elements:
  ```python
  unique_items = set(my_list)
  ```

### 3. The Time-Space Trade-off
While you don't always have to trade time for space, the **time-space trade-off** is a very common pattern in algorithm design. 

---

## Interview Strategy: Choosing the Right Approach

### Standard Safe Choices
Prioritize these in interviews when data constraints are vague, as they make the fewest assumptions about the input:

| Approach | Time Complexity | Space Complexity | Trade-off Summary |
| :--- | :--- | :--- | :--- |
| **Hash Set** | `O(n)` | `O(n)` | **Unbalanced:** Fast runtime, but requires extra memory. |
| **Sorting** | `O(n log n)` | `O(1)` or `O(log n)`* | **Balanced:** Good memory score with an acceptable runtime. |

*\*Note: Space complexity for sorting depends on the language's sorting algorithm (e.g., Python's Timsort uses `O(n)` worst-case space, while in-place heapsort uses `O(1)`).*

### Advanced Alternatives & When to Use Them
* **Hash Set or Sorting:** Best for small lists, sparse data, or numbers spanning a huge range (e.g., 64-bit IDs).
* **Bit Vector / BitSet:** Best when dealing with millions of 32-bit integers that have dense data and known boundaries.
* **Index Marking Technique:** Sometimes specifically looked for in coding interviews. 
  * *Constraint:* Only works if the problem guarantees every number falls within the range of the array's length (e.g., `[1, 2, 2]`, where values are between `0` and `3`). It will **not** work for negative numbers, floats, or numbers distributed across a massive range.

