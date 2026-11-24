Day 16 - Self Learning Log

Agenda
Leetcode:
- #206 Reverse Linked List
- #92 Reverse Linked List II
Learning:
- Core focus: In-place iterative 3-pointer manipulation (prev, curr, next); reversing a partial sublist between boundaries m and n.
- Secondary focus: AWS-Dev (course 7)
Production Code:
- Project 1: Database Engineering (Database fundamentals)

Core daily question: What is In-place iterative 3-pointer manipulation (prev, curr, next) and reversing a partial sublist between boundaries m and n?
In-place iterative 3-pointer manipulation is a technique for reversing a linked list in $O(1)$ space by walking forward and flipping each node's .next pointer backward. Because overwriting curr.next breaks your link to the rest of the list, you use three pointers—prev, curr, and next—to save the upcoming node, flip the current pointer backward, and advance forward in lockstep.
To reverse a partial sublist between boundaries $m$ and $n$, you anchor a dummy node before the head to avoid edge cases, walk to the node right before position $m$, and run that exact same 3-pointer reversal $n - m + 1$ times. Finally, you reconnect the two broken boundaries: pointing the node before $m$ to the new sublist head (prev), and pointing the original $m$-th node—now the sublist's tail—to the remaining untouched nodes (curr).
