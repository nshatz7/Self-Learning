# 20. Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Constraints
* `1 <= s.length <= 10^4`
* `s` consists of parentheses only: `'()[]{}'`

---

## Examples

| Example | Input (`s`) | Output | Explanation |
| :--- | :--- | :--- | :--- |
| **1** | `"()"` | `true` | Valid matching pair. |
| **2** | `"()[]{}"` | `true` | All pairs match and close in order. |
| **3** | `"(]"` | `false` | Mismatched bracket types. |
| **4** | `"([])"` | `true` | Nested brackets close in the correct inner-to-outer order. |
| **5** | `"([)]"` | `false` | Brackets close out of order. |

---

## Key Concepts & Notes

### Explicit Stack
An **explicit stack** is a manual data structure (typically a Python `list`) that you manage yourself in code to track state, rather than relying on the language's implicit call stack (recursion).

* **4 Core Operations** (all $O(1)$ time complexity):
  1. **Create:** `stack = []`
  2. **Push** *(add to top)*: `stack.append(val)`
  3. **Pop** *(remove and return top value)*: `stack.pop()`
  4. **Peek** *(look at top value without removing)*: `stack[-1]`

### Evaluating Operands with a Stack (Core Rules)
1. **If you see a number (operand):** Convert to an integer and push onto the stack.
2. **If you see an operator:** Pop the top two operands, apply the operator, and push the result back onto the stack.
3. **#1 Trap:** A stack reverses order when you pop—the **first** number popped is the **right** side of the equation.

### Python `match` / `case` Pattern Matching
Use `match` and `case` with `|` when checking if a single value equals one of several options (cleaner than chaining multiple `or` conditions):

```python
for num in nums:
    match num:
        case 4 | 3 | 17:  # Equivalent to: if num == 4 or num == 3 or num == 17
            pass
