# 92. Reverse Linked List II

## Problem Statement

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

### Examples

| Example | Input | Output |
| :--- | :--- | :--- |
| **Example 1** | `head = [1, 2, 3, 4, 5]`, `left = 2`, `right = 4` | `[1, 4, 3, 2, 5]` |
| **Example 2** | `head = [5]`, `left = 1`, `right = 1` | `[5]` |

### Constraints
* The number of nodes in the list is `n`.
* `1 <= n <= 500`
* `-500 <= Node.val <= 500`
* `1 <= left <= right <= n`

---

## Key Concept: Sublist Reversal ("The Train Car Analogy")

* **The Core Trick:** Attach a `dummy` node before `head` (`dummy.next = head`) so you **never** have to treat `left == 1` as a special edge case.
* Walk through the reversal in three distinct phases (using `head = [1, 2, 3, 4, 5]`, `left = 2`, `right = 4` as the model):

### Phase 1: Drop Two Sticky Notes
Before flipping any pointers, walk up to the node right before the sublist and place two reference pointers so you don't lose your anchors:

1. **Sticky Note 1 (`before_sublist`):** Place on node `1` (the node directly before position `left`).
2. **Sticky Note 2 (`sublist_tail`):** Place on node `2` (`before_sublist.next`, the first node of the section being flipped).
   * **Why?** Node `2` starts at the front of `[2 -> 3 -> 4]`. Once that section is reversed to `[4 -> 3 -> 2]`, node `2` becomes the tail of the flipped segment.

### Phase 2: Flip the Middle Section
Ignore node `1` and node `5`. Perform standard iterative pointer reversal across `[2 -> 3 -> 4]` for `right - left + 1` iterations (`3` flips total):

```text
[4] -> [3] -> [2]
```

Once the loop finishes, your two working pointers naturally land on the exact boundary nodes needed for reconnection:
* **`prev`** stands on node `4` (the new front of the reversed sublist).
* **`curr`** stands on node `5` (the untouched node immediately following position `right`).

### Phase 3: Reconnect the Train
At this moment, the list is split into three separate pieces:
* **Front piece:** `[Dummy] -> [1]` (anchored by `before_sublist`)
* **Flipped middle:** `[4] -> [3] -> [2]` (`prev` is at `4`; `sublist_tail` is at `2`)
* **Back piece:** `[5]` (`curr` is at `5`)

Stitch the two gaps back together in two assignments:
1. Hook `before_sublist` (`1`) to `prev` (`4`): `before_sublist.next = prev` (`1 -> 4`)
2. Hook `sublist_tail` (`2`) to `curr` (`5`): `sublist_tail.next = curr` (`2 -> 5`)

The full list is now seamlessly reconnected:

```text
[Dummy] -> [1] -> [4] -> [3] -> [2] -> [5]
```

Return `dummy.next`.


