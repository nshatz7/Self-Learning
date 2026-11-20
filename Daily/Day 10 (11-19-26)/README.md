# Day 10 - Self-Learning Log

## Agenda

### LeetCode
* **#155** — Min Stack
* **#739** — Daily Temperatures

### Learning Focus
* **Core Focus:** Designing $O(1)$ auxiliary state tracking & the monotonic decreasing stack pattern
* **Secondary Focus:** AWS Certified Developer (Course 1)

### Production Code
* **Project 1:** Backend Development (Query Parameters)

---

## Conclusion & Progress

### Completed
* Solved both LeetCode problems (#155 and #739) with full README documentation.
* Implemented query parameter handling in **Project 1: Backend Development**.

### Learning Outcomes
* **AWS - Dev (Course 1):**
  * AWS Shared Responsibility Model (developer perspective)
  * IAM essentials
  * Developer environment and tooling stack
  * Key exam and best-practice takeaways
* **Production Code (Query Parameters):**
  * Definition and mechanics of query parameters
  * Architecture breakdown for Project 1

---

## Core Daily Question

> **What are $O(1)$ Auxiliary State Tracking and the Monotonic Decreasing Stack Pattern?**

* **$O(1)$ Auxiliary State Tracking:** 
  Pair every element with a snapshot of the aggregate state at the exact moment that element is pushed. Because a stack follows Last-In, First-Out (LIFO) order, popping an element automatically reverts the state to the snapshot right below it in $O(1)$ time.

* **The Monotonic Decreasing Stack Pattern:** 
  Maintain elements (usually stored as indices) in strictly or non-strictly decreasing order from bottom to top to find the **Next Greater Element (NGE)** (or **Previous Greater Element (PGE)**) for every item in $O(n)$ time.
