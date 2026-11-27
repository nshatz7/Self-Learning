# 142. Linked List Cycle II

## Problem Statement

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if some node can be reached again by continuously following the `next` pointer. Internally, `pos` denotes the index of the node that the tail's `next` pointer connects to (`0`-indexed). It is `-1` if there is no cycle (`pos` is not passed as a parameter).

Do not modify the linked list.

### Examples

| Example | Input | Output | Explanation |
| :--- | :--- | :--- | :--- |
| **Example 1** | `head = [3, 2, 0, -4]`, `pos = 1` | `tail connects to node index 1` | The cycle begins at the second node (`val = 2`). |
| **Example 2** | `head = [1, 2]`, `pos = 0` | `tail connects to node index 0` | The cycle begins at the first node (`val = 1`). |
| **Example 3** | `head = [1]`, `pos = -1` | `no cycle` | No cycle exists; return `null`. |

### Constraints
* The number of nodes in the list is in the range `[0, 10^4]`.
* `-10^5 <= Node.val <= 10^5`
* `pos` is `-1` or a valid index in the linked list.

---

## Key Concept: Finding the Cycle Entry Point

Finding whether a cycle exists uses `slow` (1 step/turn) and `fast` (2 steps/turn). Locating the exact entry node adds a second phase: reset one pointer to `head`, keep the other at the collision node, and step both forward by 1 node at a time until they meet again.

### Mathematical Derivation

Define the path parameters:
* $L$ = steps from `head` to the cycle entry node.
* $C$ = number of nodes (steps) in the cycle.
* $k$ = steps from the cycle entry node forward to the initial meeting point ($0 \le k < C$).
* $C - k$ = remaining steps around the cycle from the meeting point back to the entry node.

Suppose `slow` and `fast` collide after $t$ steps taken by `slow`:

$$d_{\text{slow}} = t = L + k$$

$$d_{\text{fast}} = 2t = 2(L + k)$$

Because `fast` has completed $m \ge 1$ full loops around the cycle relative to `slow` at the moment they collide:

$$d_{\text{fast}} - d_{\text{slow}} = mC$$

Substitute $d_{\text{slow}}$ and $d_{\text{fast}}$ and solve for $L$:

$$2(L + k) - (L + k) = mC$$

$$L + k = mC$$

$$L = mC - k$$

Factor out $(m - 1)C$ so one full cycle remains alongside $C - k$:

$$L = (m - 1)C + (C - k)$$

### Geometric Interpretation
* Walking $C - k$ steps from the collision node reaches the cycle entry node.
* Adding $(m - 1)C$ steps loops around the cycle $m - 1$ extra times and returns to that same entry node.
* Walking $L$ steps from `head` also lands directly on the cycle entry node.

Moving one pointer from `head` and the other from the meeting point at 1 step per iteration guarantees they coincide at the cycle entry node after $L$ steps.

