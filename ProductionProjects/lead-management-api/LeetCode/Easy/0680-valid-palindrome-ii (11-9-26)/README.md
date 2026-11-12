# Valid Palindrome II

## Description
Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

### Examples

**Example 1:**
```text
Input: s = "aba"
Output: true
```

**Example 2:**
```text
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

---

## What I Learned

* **There is no built-in function to remove a character from a string directly (strings are immutable).**
  * **Workarounds:**
    1. **Use `.replace()` with an empty string (`""`):**
       ```python
       text = "banana"
       result = text.replace("a", "")
       print(result)
       # Output: bnn
       ```
    2. **Slice and remove by index position:**
       ```python
       result = text[:i] + text[i+1:]
       ```
       *This slices everything before index `i` and combines it with everything after index `i + 1`.*

* **How to reverse a string:**
  ```python
  text = "hello"
  reversed_text = text[::-1]
  # Output: elloh
  ```

* **Class Methods in Python:**
  * When you define methods inside a class, you must include `self` as the first parameter:
    ```python
    def test(self, test):
        pass
    ```
