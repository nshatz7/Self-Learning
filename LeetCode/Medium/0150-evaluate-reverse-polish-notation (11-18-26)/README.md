# 150. Evaluate Reverse Polish Notation

## Problem Statement
Given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation**, evaluate the expression and return an integer representing its value.

### Rules & Guarantees
* **Valid operators:** `'+'`, `'-'`, `'*'`, and `'/'`.
* Each operand may be an integer or another expression.
* Division between two integers **always truncates toward zero**.
* There will **not** be any division by zero.
* The input always represents a valid arithmetic expression in Reverse Polish Notation.
* The answer and all intermediate calculations fit in a 32-bit integer.

### Constraints
* `1 <= tokens.length <= 10^4`
* `tokens[i]` is either an operator (`"+"`, `"-"`, `"*"`, `"/"`) or an integer in the range `[-200, 200]`.

---

## Examples

| Example | Input (`tokens`) | Output | Explanation |
| :--- | :--- | :--- | :--- |
| **1** | `["2","1","+","3","*"]` | `9` | `((2 + 1) * 3) = 9` |
| **2** | `["4","13","5","/","+"]` | `6` | `(4 + (13 / 5)) = 6` |
| **3** | `["10","6","9","3","+","-11","*","/","*","17","+","5","+"]` | `22` | See step-by-step breakdown below |

### Example 3 Breakdown
```text
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
