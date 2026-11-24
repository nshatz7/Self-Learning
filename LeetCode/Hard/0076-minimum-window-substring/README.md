# 76. Minimum Window Substring

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

> The test cases will be generated such that the answer is unique.

### Examples

| Example | Input | Output | Explanation |
| :--- | :--- | :--- | :--- |
| **Example 1** | `s = "ADOBECODEBANC"`, `t = "ABC"` | `"BANC"` | The minimum window substring `"BANC"` includes `'A'`, `'B'`, and `'C'` from string `t`. |
| **Example 2** | `s = "a"`, `t = "a"` | `"a"` | The entire string `s` is the minimum window. |
| **Example 3** | `s = "a"`, `t = "aa"` | `""` | Both `'a'`s from `t` must be included in the window. Since `s` only has one `'a'`, return `""`. |

### Constraints
* `m == s.length`, `n == t.length`
* `1 <= m, n <= 10^5`
* `s` and `t` consist of uppercase and lowercase English letters.

---

## Key Concept: Auxiliary Demand Tracking ("Debt & Satisfaction")

Instead of comparing two frequency maps at every step (which costs `O(K)` time where `K` is the alphabet size), track **unresolved debt** in `O(1)` per pointer movement:

1. **Demand Map (`need`):** Store the required count of each character from `t`.
2. **Missing Counter (`missing`):** Initialize to `len(t)`. This represents the total number of required characters still owed to make the window valid.
3. **Expand (`right` pointer):**
   * As `s[right]` enters the window, check if `need[char] > 0`. If so, this character pays off part of your debt—decrement `missing`.
   * Always decrement `need[char]`. Characters not in `t` (or extra duplicates) naturally drop into negative numbers, representing a **"surplus"**.
4. **Contract (`left` pointer):**
   * Once `missing == 0`, the window is valid. Shrink from the left to minimize the window length until validity breaks:
     * Update the minimum window bounds (`start`, `end`) if `right - left + 1` is a new minimum.
     * Before removing `s[left]`, increment `need[s[left]]`.
     * If `need[s[left]] > 0`, you just evicted a critical character that had zero surplus. Increment `missing`, which exits the contraction loop and forces `right` to expand again.

