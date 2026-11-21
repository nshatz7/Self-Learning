# 424. Longest Repeating Character Replacement

## Problem Statement

Given a string `s` and an integer `k`, you can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Examples

**Example 1:**
- **Input:** `s = "ABAB"`, `k = 2`
- **Output:** `4`
- **Explanation:** Replace the two `'A'`s with two `'B'`s or vice versa.

**Example 2:**
- **Input:** `s = "AABABBA"`, `k = 1`
- **Output:** `4`
- **Explanation:** Replace the one `'A'` in the middle with `'B'` to form `"AABBBBA"`. The substring `"BBBB"` has the longest repeating letters, which is `4`. (Other valid replacements also achieve `4`.)

### Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## Key Concepts Learned

### Tracking Max Frequency Count (Majority Rule)
- **The Rule:** You can replace at most `k` characters to make the entire window consist of a single repeating character.
- **The State:** 
  - A frequency map `counts` tracking the occurrences of characters in the current window.
  - A single integer `max_freq` tracking the highest count of any single character seen in a window.
- **Window Validity Formula:**
  To make all characters in a window of size `window_len` identical, keep the most frequent character and replace everything else:
  - **Replacements Needed:** `window_len - max_freq`
  - **Valid Window:** `(right - left + 1) - max_freq <= k`
  - **Invalid Window:** `(right - left + 1) - max_freq > k`
- **Shrinking Behavior:** When the window becomes invalid, shift `left` forward by `1` (decrementing `counts[s[left]]`).


