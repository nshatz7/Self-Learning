# 21. Merge Two Sorted Lists

## Problem Statement

Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into one sorted list. The list should be made by **splicing together** the nodes of the first two lists.

Return the `head` of the merged linked list.

### Examples

| Example | Input | Output |
| :--- | :--- | :--- |
| **Example 1** | `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]` | `[1, 1, 2, 3, 4, 4]` |
| **Example 2** | `list1 = []`, `list2 = []` | `[]` |
| **Example 3** | `list1 = []`, `list2 = [0]` | `[0]` |

### Constraints
* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in **non-decreasing** order.

---

## Key Concept: Why Sentinel (`dummy`) Head Nodes Exist

When constructing or splicing a linked list from existing nodes, managing the `head` pointer is often the trickiest part:
* You do not know whether `list1` or `list2` holds the smaller initial element until you compare them.
* Without a sentinel node, your code needs special initialization logic (`if / else`) just to set the real `head` and `tail` on the very first node.

### How the Sentinel Pattern Works
1. Allocate a placeholder node (`dummy = ListNode(0)`) and set a builder pointer `curr = dummy`.
2. While both `list1` and `list2` are non-empty:
   * Compare `list1.val` and `list2.val`.
   * Attach the smaller node to `curr.next`, advance that list's pointer forward, and advance `curr = curr.next`.
3. Once one list is exhausted, attach the remaining non-empty list directly to `curr.next` (`curr.next = list1 or list2`).
4. Return `dummy.next`.

### Why It Matters
* **Uniform Loop Logic:** Every step follows the exact same attachment and advancement pattern—no special cases for the first element or empty lists.
* **Fewer Pointer Bugs:** Eliminates awkward `head` initialization checks and reduces null-pointer or off-by-one mistakes.

---

## Complexity Analysis

* **Time Complexity:** `O(n + m)` — Where `n` and `m` are the lengths of `list1` and `list2`; each node is visited and spliced once.
* **Space Complexity:** `O(1)` — Nodes are re-linked in-place using only a constant number of pointers (`dummy`, `curr`).
