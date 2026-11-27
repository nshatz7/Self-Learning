Day 18 - Self Learning Log

Agenda
Leetcode:
- #141 Linked list cycle
- #142 Linked list cycle II
Learning:
- Core focus: Floyd’s Tortoise and Hare algorithm; mathematical derivation to locate the exact cycle entry node.
- Secondary focus: AWS-Dev (course 9)
Production Code:
- Project 1: Database Engineering (PostgreSQL setup)




Core daily question: What is Floyd’s Tortoise and Hare algorithm, and mathematical derivation to locate the exact cycle entry node?

Finding the Cycle Entry Point
Finding whether a cycle exists uses slow (1 step/turn) and fast (2 steps/turn). Locating the exact entry node adds a second phase: reset one pointer to head, keep the other at the collision node, and step both forward by 1 node at a time until they meet again.

Mathematical Derivation
Define the path parameters:

L
 = steps from head to the cycle entry node.
C
 = number of nodes (steps) in the cycle.
k
 = steps from the cycle entry node forward to the initial meeting point (
0
≤
k
<
C
).
C
−
k
 = remaining steps around the cycle from the meeting point back to the entry node.
Suppose slow and fast collide after 
t
 steps taken by slow:

d
slow
=
t
=
L
+
k

d
fast
=
2
t
=
2
(
L
+
k
)

Because fast has completed 
m
≥
1
 full loops around the cycle relative to slow at the moment they collide:

d
fast
−
d
slow
=
m
C

Substitute 
d
slow
 and 
d
fast
 and solve for 
L
:

2
(
L
+
k
)
−
(
L
+
k
)
=
m
C

L
+
k
=
m
C

L
=
m
C
−
k

Factor out 
(
m
−
1
)
C
 so one full cycle remains alongside 
C
−
k
:

L
=
(
m
−
1
)
C
+
(
C
−
k
)

Geometric Interpretation
Walking 
C
−
k
 steps from the collision node reaches the cycle entry node.
Adding 
(
m
−
1
)
C
 steps loops around the cycle 
m
−
1
 extra times and returns to that same entry node.
Walking 
L
 steps from head also lands directly on the cycle entry node.
Moving one pointer from head and the other from the meeting point at 1 step per iteration guarantees they coincide at the cycle entry node after 
L
 steps.





 Tortoise and Hare Algorithm (Floyd's Cycle Detection) Initialize two pointers at head: slow (tortoise): Advances 1 node per step (slow = slow.next). fast (hare): Advances 2 nodes per step (fast = fast.next.next). Loop Condition & Termination Loop while fast and fast.next are non-null: If there is no cycle, fast (or fast.next) hits null and the loop ends, returning false. If there is a cycle, both pointers eventually enter the loop. Once both are inside a cycle of finite length C , fast gains 1 position on slow per iteration (relative speed of 1 node per step). Because the gap shrinks by 1 each step, the distance between them reaches 0 within at most C steps—at which point slow == fast, returning true.

