# 3. Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the **longest substring** without duplicate characters.

### Examples

**Example 1:**
* **Input:** `s = "abcabcbb"`
* **Output:** `3`
* **Explanation:** The answer is `"abc"`, with a length of `3`. *(Note: `"bca"` and `"cab"` are also valid answers).*

**Example 2:**
* **Input:** `s = "bbbbb"`
* **Output:** `1`
* **Explanation:** The answer is `"b"`, with a length of `1`.

**Example 3:**
* **Input:** `s = "pwwkew"`
* **Output:** `3`
* **Explanation:** The answer is `"wke"`, with a length of `3`. *(Note: The answer must be a contiguous substring; `"pwke"` is a subsequence and not a substring).*

### Constraints
* $0 \le \text{s.length} \le 10^5$
* `s` consists of English letters, digits, symbols, and spaces.

---

## Key Takeaways & Concepts

### 1. Tracking Character Sets in a Dynamic Window
**The Mechanics: The "Expand-Until-Conflict" Loop**
Think of the `right` pointer as the **explorer** and the `left` pointer as the **cleanup crew**:

1. **Expand (`right` moves right):** The explorer tries to step onto `s[right]`.
2. **Conflict Check:** Before accepting `s[right]`, check the `Set`. If `s[right]` is already in the `Set`, adding it would violate the uniqueness rule.
3. **Contract (`left` moves right):** The cleanup crew advances `left`, deleting `s[left]` from the `Set` at every step until the previous copy of `s[right]` is evicted.
4. **Commit:** Now that the conflict is cleared, add the new `s[right]` to the `Set` and record the window's size (`right - left + 1`).

### 2. Upgrading from a Set to an Index Map ("Teleporting `left`")
* **The Bottleneck:** If a duplicate character is 500 indices behind `right`, a standard `while` loop has to step `left` forward 500 times one-by-one.
* **The Fix:** Store characters and their positions in a dictionary/hash map formatted as `{character: last_seen_index}`. This allows the `left` pointer to "teleport" directly past the duplicate in a single $O(1)$ operation.
