# 448. Find All Numbers Disappeared in an Array

## Problem Statement
Given an array `nums` of $n$ integers where `nums[i]` is in the range $[1, n]$, return an array of all the integers in the range $[1, n]$ that do not appear in `nums`.

### Examples
**Example 1:**
* **Input:** `nums = [4,3,2,7,8,2,3,1]`
* **Output:** `[5,6]`

**Example 2:**
* **Input:** `nums = [1,1]`
* **Output:** `[2]`

### Constraints
* $n == \text{nums.length}$
* $1 \le n \le 10^5$
* $1 \le \text{nums}[i] \le n$

---

## Key Concept: In-Place Array Sign Marking

### How It Works
Using the input array itself as a hash table, you negate the number at the corresponding target index (`nums[index] *= -1`) to mark that value as "seen."

### Complexity & Trade-offs
* **Time Complexity:** $O(n)$
* **Auxiliary Space Complexity:** $O(1)$
* **Caveat:** This optimization is only possible because the problem guarantees that all values fall strictly within the bounded range $[1, n]$.

### When to Use a Hash Set (Streak Routes) Instead
In-place sign marking is a specialized trick. You should default to a standard Hash Set in the following scenarios:
1. **Negative Numbers or Zeros:** If the array contains `0` or negative integers, sign marking breaks immediately.
2. **Unbounded Values:** If the numbers in the array can be larger than the array's length ($n$), indexing into the array will crash with an `IndexError`.
3. **Immutability / Data Preservation:** Sign marking is destructive—it mutates the input array. If you need to preserve the original values or reuse the array later, you would have to do an extra pass to restore all numbers back to positive.

### Real-World Analogy / Scenario
Imagine you have a list of locker numbers assigned to students, and the locker IDs are strictly between $1$ and $n$ (where $n$ is the total number of lockers). Some students have accidentally been assigned the same locker. You want to flag a warning every time a locker is double-booked, without allocating extra memory for a new list or set. By flipping the sign at each locker's index as you check student assignments, hitting an already-negative number immediately alerts you to a duplicate booking.
