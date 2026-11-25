# 23. Merge k Sorted Lists

## Problem Statement

Given an array of `k` linked-lists `lists`, each linked-list is sorted in **ascending order**.

Merge all the linked-lists into one sorted linked-list and return it.

### Examples

| Example | Input | Output | Explanation |
| :--- | :--- | :--- | :--- |
| **Example 1** | `lists = [[1,4,5],[1,3,4],[2,6]]` | `[1,1,2,3,4,4,5,6]` | Merging `1->4->5`, `1->3->4`, and `2->6` produces `1->1->2->3->4->4->5->6`. |
| **Example 2** | `lists = []` | `[]` | No lists to merge. |
| **Example 3** | `lists = [[]]` | `[]` | Single empty list. |

### Constraints
* `k == lists.length`
* `0 <= k <= 10^4`
* `0 <= lists[i].length <= 500`
* `-10^4 <= lists[i][j] <= 10^4`
* `lists[i]` is sorted in ascending order.
* The sum of `lists[i].length` will not exceed `10^4`.

---

## Key Concept: Divide-and-Conquer Pairwise Merge (`O(N log k)`)

Instead of merging sequentially from left to right (which repeatedly re-traverses already-merged nodes and costs up to `O(N * k)`), pair up lists and merge two sorted lists at a time across rounds—mirroring the merge stage of Merge Sort:

* **Round 1:** `k` lists merge in `k / 2` pairs. Each pair merges in linear time of its combined elements, so total work across all pairs in the round is `O(N)` (where `N` is the total number of nodes across all lists).
* **Round 2:** `k / 2` resulting lists merge in `k / 4` pairs, again taking `O(N)` total work across the round.
* **Subsequent Rounds:** Continue halving the active list count (`k / 8`, `k / 16`, ...) until a single sorted list remains.

With `log2(k)` rounds and `O(N)` work per round, the total time complexity is `O(N log k)`.


