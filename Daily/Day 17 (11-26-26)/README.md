# Day 17 — Self-Learning Log

## Agenda

| Category | Focus Areas |
| :--- | :--- |
| **LeetCode** | • **#21** Merge Two Sorted Lists<br>• **#23** Merge k Sorted Lists |
| **Core Learning** | Sentinel/dummy head nodes; scaling from 2 pointers to a priority queue (`O(N log k)`) or divide-and-conquer merge |
| **Secondary Learning** | AWS-Dev (Course 8) |
| **Production Code** | **Project 1:** Database Engineering (SQL Fundamentals) |

---

## Conclusion & Progress

### Completed Tasks
- [x] **LeetCode:** Solved #21 & #23 with full READMEs
- [x] **Project 1:** Database Engineering (SQL Fundamentals)

### Key Learning Outcomes

#### AWS-Dev — Course 8
* Asynchronous Processing & Decoupling (Amazon SQS, Amazon SNS, Amazon EventBridge, AWS Step Functions)

#### Production Code — Database Engineering
* SQL Fundamentals (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) mapped to the Lead Management API

---

## Core Daily Question

> **What are sentinel/dummy head nodes, and how do you scale from 2 pointers to a priority queue (`O(N log k)`) or divide-and-conquer merge?**

### 1. Sentinel / Dummy Head Nodes
When building or splicing a linked list, initializing the real `head` pointer usually requires special conditional branching because you do not know which input list contains the smallest initial node. A sentinel node removes that edge case entirely.

#### How the Sentinel Pattern Works
1. Allocate a placeholder node (`dummy = ListNode(0)`) and initialize a builder pointer `curr = dummy`.
2. While both `list1` and `list2` are non-empty:
   * Compare `list1.val` and `list2.val`.
   * Attach the smaller node to `curr.next`, advance that list's pointer forward, and advance `curr = curr.next`.
3. Once one list is exhausted, attach the remaining non-empty list directly to `curr.next` (`curr.next = list1 or list2`).
4. Return `dummy.next`.

#### Why It Matters
* **Uniform Loop Logic:** Every step follows the exact same attachment and advancement pattern—no special cases for the first element or empty lists.
* **Fewer Pointer Bugs:** Eliminates awkward `head` initialization checks and reduces null-pointer or off-by-one mistakes.

---

### 2. Scaling from 2 Pointers to `k` Lists (`O(N log k)`)
Comparing `k` list heads linearly at every step costs `O(N * k)` time, and merging lists sequentially one-by-one re-traverses already-merged nodes repeatedly. Two patterns drop the runtime to `O(N log k)`:

* **Min-Heap (Priority Queue):** Store the current head of each non-empty list in a min-heap of size at most `k`. Popping the smallest node and pushing its `.next` takes `O(log k)` per node across `N` total nodes, yielding `O(N log k)` time and `O(k)` space.
* **Divide-and-Conquer Pairwise Merge:** Pair up lists and merge two sorted lists at a time across rounds—mirroring the merge stage of Merge Sort:
  * **Round 1:** `k` lists merge in `k / 2` pairs. Each pair merges in linear time of its combined elements, so total work across all pairs in the round is `O(N)` (where `N` is the total number of nodes across all lists).
  * **Round 2:** `k / 2` resulting lists merge in `k / 4` pairs, again taking `O(N)` total work across the round.
  * **Subsequent Rounds:** Continue halving the active list count (`k / 8`, `k / 16`, ...) until a single sorted list remains.
  * With `log2(k)` rounds and `O(N)` work per round, the total time complexity is `O(N log k)`.

