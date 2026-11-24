# 567. Permutation in String

> **Difficulty:** Medium  
> **Topics:** Hash Table, Two Pointers, String, Sliding Window

---

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

### Examples

* **Example 1:**
  ```text
  Input: s1 = "ab", s2 = "eidbaooo"
  Output: true
  Explanation: s2 contains one permutation of `s1` ("ba").
  ```

* **Example 2:**
  ```text
  Input: s1 = "ab", s2 = "eidboaoo"
  Output: false
  ```

### Constraints

* $1 \le \text{s1.length}, \text{s2.length} \le 10^4$
* `s1` and `s2` consist of lowercase English letters.

---

## Key Concepts & Takeaways

### 1. Fixed Sliding Window
* **Definition:** A contiguous subarray or substring of a locked length $k$ (where $k = \text{s1.length}$) that moves across a sequence one step at a time from left to right.
* **Application:** Since any permutation of `s1` must have the exact same length as `s1`, we only need to inspect windows of size `s1.length` inside `s2`. As the window slides right by one character, we add the new character entering from the right and remove the old character exiting from the left.

### 2. Array-Based Character Frequency Map
* **Definition:** When working exclusively with lowercase English letters (`'a'` through `'z'`), we can use a fixed-size array of 26 integers (`'a' = 0`, `'b' = 1`, ..., `'z' = 25`) instead of a standard hash map.
* **Application:** Provides true $O(1)$ lookups, insertions, and space complexity ($O(26) \rightarrow O(1)$), avoiding the memory overhead and hashing collisions of a dynamic dictionary/hash map.

### 3. Maintaining the `matches` Counter
* **Definition:** A single integer variable that tracks how many of the 26 alphabet buckets currently have identical character frequencies in both `s1` and the current window of `s2`.
* **Application:** Eliminates the need to scan and compare all 26 buckets at every step of the sliding window. When `matches == 26`, every character frequency aligns, meaning we have found a valid permutation in $O(1)$ check time.
