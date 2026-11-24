# 206. Reverse Linked List

## Problem Statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### Examples

| Example | Input | Output |
| :--- | :--- | :--- |
| **Example 1** | `head = [1, 2, 3, 4, 5]` | `[5, 4, 3, 2, 1]` |
| **Example 2** | `head = [1, 2]` | `[2, 1]` |
| **Example 3** | `head = []` | `[]` |

### Constraints
* The number of nodes in the list is in the range `[0, 5000]`.
* `-5000 <= Node.val <= 5000`

---

## Key Concept: Iterative In-Place Pointer Reversal

To reverse a singly linked list in `O(1)` auxiliary space, you cannot walk backward. Instead, walk forward through the list while flipping each node's `.next` pointer to point to the node behind it.

### The Three Pointers
1. **`prev`:** Tracks the node behind `curr` (initialized to `None` / `null`, since the original `head` becomes the new tail).
2. **`curr`:** Tracks the node whose pointer is currently being reversed (initialized to `head`).
3. **`next_temp`:** A temporary bookmark saving `curr.next` before overwriting it so you don't lose access to the remainder of the list.

### The 4-Step Loop (While `curr` is not `None`)
1. **Save:** `next_temp = curr.next` — Hold onto the rest of the unreversed list.
2. **Reverse:** `curr.next = prev` — Flip the current node's pointer backward.
3. **Advance `prev`:** `prev = curr` — Move `prev` up to the node you just fixed.
4. **Advance `curr`:** `curr = next_temp` — Jump forward to your saved bookmark.

Once `curr` reaches `None`, `prev` sits at the new head of the reversed list.

