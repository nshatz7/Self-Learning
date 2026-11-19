# 155. Min Stack

## Problem Statement

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
* `MinStack()` initializes the stack object.
* `void push(int val)` pushes the element `val` onto the stack.
* `void pop()` removes the element on the top of the stack.
* `int top()` gets the top element of the stack.
* `int getMin()` retrieves the minimum element in the stack.

> **Requirement:** You must implement a solution with $O(1)$ time complexity for each function.

---

### Example 1

**Input:**
```text
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

**Output:**
```text
[null,null,null,null,-3,null,0,-2]
```

**Explanation:**
```python
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin() # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin() # return -2
```

### Constraints
* $-2^{31} \le \text{val} \le 2^{31} - 1$
* Methods `pop`, `top`, and `getMin` operations will always be called on **non-empty** stacks.
* At most $3 \times 10^4$ calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## Key Takeaways: $O(1)$ Auxiliary State Tracking

### The Core Problem
In a standard stack, `push` and `pop` are $O(1)$, but finding the minimum element requires scanning the entire stack ($O(n)$). Simply keeping a single `min_val` variable fails when that minimum element is popped—you wouldn't know what the next smallest element was before it arrived.

### The Design Pattern
Pair every element with a **snapshot of the aggregate state** at the exact moment that element was pushed. Because stacks follow Last-In, First-Out (LIFO), popping an element automatically reverts the state to the snapshot right below it.

### Implementation (Python)
You can implement this using two parallel stacks, or a single stack storing `(value, current_min)` tuples:

```python
class MinStack:

    def __init__(self):
        # Stores tuples of (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

### Complexity Analysis
* **Time Complexity:** O(1) for `push`, `pop`, `top`, and `getMin`.
* **Space Complexity:** O(n) to store the auxiliary minimum snapshots alongside the n elements in the stack.
