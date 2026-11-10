# 383. Ransom Note

## Problem Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine`, and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Examples

#### Example 1
- **Input:** `ransomNote = "a"`, `magazine = "b"`
- **Output:** `false`

#### Example 2
- **Input:** `ransomNote = "aa"`, `magazine = "ab"`
- **Output:** `false`

#### Example 3
- **Input:** `ransomNote = "aa"`, `magazine = "aab"`
- **Output:** `true`

### Constraints
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

---

## Key Takeaways & Concepts

### 1. `ord()` and Fixed-Size Arrays (Space Optimization)
Using a fixed-size integer array instead of a hash map (`dict` or `Counter`) eliminates the memory overhead of dynamic hashing.

- **`ord(char)`**: Returns the Unicode integer value of a given character.
  - `ord('a') == 97`, `ord('b') == 98`, ..., `ord('z') == 122`
- **Zero-indexing characters**: By subtracting `ord('a')`, any lowercase English letter maps directly to an index between `0` and `25`:
  ```python
  index = ord(char) - ord('a')
  ```
- **Why this beats `Counter()` in space:**
  - `Counter()` or dynamic hash tables store keys, values, hash buckets, and overhead for collision resolution.
  - A fixed array `[0] * 26` allocates exactly 26 integer slots up front, maintaining a strict $O(1)$ auxiliary space footprint with virtually zero allocation overhead.

---

## Solutions

### Approach 1: Fixed-Size Array (Optimal Space & Runtime)
Count frequencies in `magazine`, then decrement while checking `ransomNote`. If any count drops below zero, `magazine` cannot form the note.

- **Time Complexity:** $O(m + n)$ — where $m$ is `len(magazine)` and $n$ is `len(ransomNote)`.
- **Space Complexity:** $O(1)$ — Array size is strictly fixed at 26 elements.

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Quick exit: ransomNote can't be made if it needs more characters than magazine has
        if len(ransomNote) > len(magazine):
            return False

        counts = [0] * 26
        base = ord('a')

        for char in magazine:
            counts[ord(char) - base] += 1

        for char in ransomNote:
            idx = ord(char) - base
            counts[idx] -= 1
            if counts[idx] < 0:
                return False

        return True
```

### Approach 2: Using `collections.Counter` (Concise Alternative)
Subtracting counters in Python keeps only positive remaining counts. If the difference between the note and the magazine is empty, all characters were satisfied.

- **Time Complexity:** $O(m + n)$
- **Space Complexity:** $O(k)$ — at most 26 keys in the hash map, but with higher hash table overhead.

```python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter subtraction (ransomNote - magazine) leaves only counts where ransomNote exceeds magazine
        return not Counter(ransomNote) - Counter(magazine)
```
