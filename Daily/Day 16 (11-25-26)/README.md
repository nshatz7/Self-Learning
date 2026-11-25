# Day 16 — Self-Learning Log

## Agenda

| Category | Focus Areas |
| :--- | :--- |
| **LeetCode** | • **#206** Reverse Linked List<br>• **#92** Reverse Linked List II |
| **Core Learning** | In-place iterative 3-pointer manipulation (`prev`, `curr`, `next`); reversing a partial sublist between boundaries `m` and `n` |
| **Secondary Learning** | AWS-Dev (Course 7) |
| **Production Code** | **Project 1:** Database Engineering (Database Fundamentals) |

---

## Conclusion & Progress

### Completed Tasks
- [x] **LeetCode:** Solved #206 & #92 with full READMEs
- [x] **Project 1:** Database Engineering (Database Fundamentals)

### Key Learning Outcomes

#### AWS-Dev — Course 7
* The Lambda Execution Environment Lifecycle & Execution Context Reuse
* Memory-to-CPU Scaling & Cold Start Mitigation (Provisioned Concurrency vs. SnapStart)
* Concurrency Controls (Reserved vs. Provisioned)
* Packaging, Layers, Extensions, & Versioning / Aliases
* VPC Networking & Amazon RDS Proxy

#### Production Code — Database Engineering
* Database fundamentals for Project 1

---

## Core Daily Question

> **What is in-place iterative 3-pointer manipulation (`prev`, `curr`, `next`) and reversing a partial sublist between boundaries `m` and `n`?**

### 1. In-Place Iterative 3-Pointer Manipulation
In-place iterative 3-pointer manipulation is a technique for reversing a linked list in `O(1)` auxiliary space by walking forward and flipping each node's `.next` pointer backward. Because overwriting `curr.next` breaks your link to the rest of the list, you use three pointers—`prev`, `curr`, and `next`—to save the upcoming node, flip the current pointer backward, and advance forward in lockstep:

1. **Save:** `next = curr.next` (preserve the remaining nodes).
2. **Flip:** `curr.next = prev` (point the current node backward).
3. **Advance:** `prev = curr` and `curr = next` (step both pointers forward).

---

### 2. Reversing a Partial Sublist Between Boundaries `m` and `n`
To reverse a partial sublist between boundaries `m` and `n`:

1. **Anchor & Locate:** Attach a `dummy` node before `head` so `m == 1` requires no special edge-case handling, then walk forward to the node immediately preceding position `m`.
2. **Reverse the Slice:** Run the same 3-pointer reversal across `n - m + 1` nodes within the target range.
3. **Reconnect Boundaries:** Link the two seams back together—point the node before `m` to the new head of the reversed sublist (`prev`), and point the original `m`-th node (now the tail of the reversed slice) to the remaining untouched nodes (`curr`).
