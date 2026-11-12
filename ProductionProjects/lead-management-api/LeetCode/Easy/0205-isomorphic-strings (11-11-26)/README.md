# 205. Isomorphic Strings

## Problem Description
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

- All occurrences of a character must be replaced with another character while preserving the order of characters.
- No two characters may map to the same character, but a character may map to itself.

---

## Examples

### Example 1
- **Input:** `s = "egg"`, `t = "add"`
- **Output:** `true`
- **Explanation:**
  The strings `s` and `t` can be made identical by:
  - Mapping `'e'` to `'a'`
  - Mapping `'g'` to `'d'`

### Example 2
- **Input:** `s = "f11"`, `t = "b23"`
- **Output:** `false`
- **Explanation:**
  The strings `s` and `t` cannot be made identical because `'1'` needs to be mapped to both `'2'` and `'3'`.

### Example 3
- **Input:** `s = "paper"`, `t = "title"`
- **Output:** `true`

---

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ASCII character.

---

## Key Takeaways & Concepts

- **`zip()`**: Combines elements from multiple iterables (lists, tuples, strings) into a single iterable of paired tuples based on their index.
- **Bi-directional Mapping**: Ensures a strict one-to-one (bijective) mapping between characters. Using two hash maps (or checking both directions) prevents multiple characters from mapping to the same target character.
