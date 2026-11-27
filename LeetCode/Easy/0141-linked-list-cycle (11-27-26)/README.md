# 141. Linked List Cycle

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists in a linked list if some node can be reached again by continuously following the `next` pointer. Internally, `pos` denotes the index of the node that the tail's `next` pointer connects to (`pos` is not passed as a parameter).

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Examples

| Example | Input | Output | Explanation |
| :--- | :--- | :---: | :--- |
| **Example 1** | `head = [3, 2, 0, -4]`, `pos = 1` | `true` | The tail (`-4`) connects back to index `1` (`2`). |
| **Example 2** | `head = [1, 2]`, `pos = 0` | `true` | The tail (`2`) connects back to index `0` (`1`). |
| **Example 3** | `head = [1]`, `pos = -1` | `false` | No cycle; the list terminates at `null`. |

### Constraints
* The number of nodes in the list is in the range `[0, 10^4]`.
* `-10^5 <= Node.val <= 10^5`
* `pos` is `-1` or a valid index in the linked list.

---

## Key Concept: Tortoise and Hare Algorithm (Floyd's Cycle Detection)

Initialize two pointers at `head`:
* **`slow` (tortoise):** Advances 1 node per step (`slow = slow.next`).
* **`fast` (hare):** Advances 2 nodes per step (`fast = fast.next.next`).

### Loop Condition & Termination
Loop while `fast` and `fast.next` are non-null:
* If there is **no cycle**, `fast` (or `fast.next`) hits `null` and the loop ends, returning `false`.
* If there is **a cycle**, both pointers eventually enter the loop. Once both are inside a cycle of finite length $C$, `fast` gains 1 position on `slow` per iteration (relative speed of 1 node per step). Because the gap shrinks by $1$ each step, the distance between them reaches $0$ within at most $C$ steps—at which point `slow == fast`, returning `true`.

