# 242. Valid Anagram

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples

#### Example 1
- **Input:** `s = "anagram"`, `t = "nagaram"`
- **Output:** `true`

#### Example 2
- **Input:** `s = "rat"`, `t = "car"`
- **Output:** `false`

### Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Key Takeaways & Concepts

### 1. `enumerate()`
- Built-in Python function that wraps an iterable and yields `(index, value)` tuples.
- **Syntax:**
```python
for idx, char in enumerate("cat"):
    print(idx, char)
# (0, 'c'), (1, 'a'), (2, 't')
```

### 2. Hash Map (Dictionary) Basics
- Stores data as `key: value` pairs: `hash_map = {key: value}`.
- Retrieve a value using its key:
```python
char_counts = {"a": 3, "n": 1}
val = char_counts["a"]  # returns 3
```

### 3. `collections.Counter`
A specialized dictionary subclass designed for counting hashable objects.

- **Import:**
```python
from collections import Counter
```
- **Usage:**
  - Works on any hashable iterable (strings, lists, tuples; not raw `int` or `float` unless converted to strings).
  - Always capitalized: `Counter()`.
  - Pass an iterable:
    ```python
    Counter("mississippi")
    # Output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
    ```
  - Pass keyword arguments:
    ```python
    Counter(cats=4, dogs=3)
    # Output: Counter({'cats': 4, 'dogs': 3})
    ```
- **Ordering Behavior:**
  - Standard dictionary and `Counter` underlying storage preserves insertion order.
  - `.most_common()` returns elements sorted from highest to lowest count.

### 4. `sorted()`
Built-in function that takes any iterable (strings, lists, tuples, dictionaries, etc.) and returns a **new list** with the elements in ascending order.

- **Basic Usage:**
```python
sorted([3, 1, 2])       # [1, 2, 3]
sorted("anagram")       # ['a', 'a', 'a', 'g', 'm', 'n', 'r']
```
- **Reverse Order:**
```python
sorted("anagram", reverse=True)  # ['r', 'n', 'm', 'g', 'a', 'a', 'a']
```
- **Custom Sorting (`key` parameter):**
  Accepts a function that transforms each element before sorting.
  ```python
  words = ["banana", "pie", "apple"]
  sorted(words, key=len)  # ['pie', 'apple', 'banana'] (shortest to longest)
  ```

### 5. `lambda` Functions
Small, anonymous, one-line functions defined without the standard `def` keyword.

- **Syntax:**
  ```python
  lambda arguments: expression
  ```
- **Basic Example:**
```python
square = lambda x: x ** 2
print(square(5))  # 25
```
- **Using `lambda` with `sorted()`:**
  Ideal for sorting complex or nested data structures (e.g., lists of dictionaries):
```python
students = [
    {"name": "Harry", "score": 85},
    {"name": "Leo", "score": 91},
    {"name": "Eve", "score": 78}
]

# Sort dictionaries by the 'score' key
sorted_students = sorted(students, key=lambda x: x["score"])
# Output: [{'name': 'Eve', 'score': 78}, {'name': 'Harry', 'score': 85}, {'name': 'Leo', 'score': 91}]
```

---

## Solutions

### Approach 1: Frequency Map with `Counter` (Optimal)
- **Time Complexity:** $O(n)$ — Single pass count over both strings.
- **Space Complexity:** $O(1)$ — At most 26 lowercase English alphabet characters stored.

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

### Approach 2: Sorting
- **Time Complexity:** O(n \log n) — Timsort on both strings.
- **Space Complexity:** O(n) or O(1) — Depending on Python list allocation for `sorted()`.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
