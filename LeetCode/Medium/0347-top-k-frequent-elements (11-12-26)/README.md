# 347. Top K Frequent Elements

## Problem Description
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

---

## Examples

### Example 1
* **Input:** `nums = [1,1,1,2,2,3]`, `k = 2`
* **Output:** `[1,2]`

### Example 2
* **Input:** `nums = [1]`, `k = 1`
* **Output:** `[1]`

### Example 3
* **Input:** `nums = [1,2,1,2,1,2,3,1,3,2]`, `k = 2`
* **Output:** `[1,2]`

---

## Constraints
* $1 \le \text{nums.length} \le 10^5$
* $-10^4 \le \text{nums}[i] \le 10^4$
* `k` is in the range `[1, the number of unique elements in the array]`.
* It is **guaranteed** that the answer is unique.

---

## Key Takeaways & Notes
* **Getting Dictionary Keys:** `my_dict.keys()` retrieves only the keys from a dictionary.
* **Finding Most Common Elements (`Counter`):** Using `.most_common(n)` on a `collections.Counter` object returns a list of the `n` most common elements and their counts as `(element, count)` tuples:
  ```python
  # Outputs the 2 most common (key, count) pairs
  counts.most_common(2)
  ```
* **Extracting Only the Top Keys:** You can combine `.most_common(k)` with a list comprehension to extract just the elements (keys) without their counts:
  ```python
  # Returns just the keys for the top 2 most common elements
  top_keys = [key for key, count in counts.most_common(2)]
  ```
