# Day 1 — Self-Learning Log

---

## Daily Agenda

* Create and initialize the `self-learning` repository
* LeetCode Practice
  * #217 — Contains Duplicate
  * #680 — Valid Palindrome II
* Core Study Topics
  * Core Focus: Hash Set vs. Single-Pass Complement Hash Map
  * Secondary: PCAP (Certified Associate in Python Programming) Exam Prep

---

## Summary & Completed Tasks

* Repository Setup: Created `self-learning` repository structure.
* Problem Solving: Completed both LeetCode problems with comprehensive problem write-ups and README notes.

---

## Key Learning Outcomes

### 1. Data Structures & Algorithms (LeetCode)
* Hash Sets: Ideal for membership testing ($\mathcal{O}(1)$ average lookup) when only checking presence or uniqueness.
* Hash Maps: Necessary when pairing values with supplementary metadata (such as indices or frequencies).

### 2. Python Fundamentals (PCAP Prep)
* Modules & Packages:
  * Working with the Python Standard Library.
  * Creating custom modules and directory structures for packages.
* Namespaces & Imports: Understanding scoping rules and syntax (`import`, `from ... import`, aliasing).
* Package Management: Using `pip` to install, manage, and inspect dependencies.

---

## Core Daily Question

> Q: When should you use a Hash Set lookup vs. a Single-Pass Complement Hash Map?

* Hash Set (`set`):
  * Use case: Checking existence or membership (e.g., whether a list or string contains a duplicate item, outputting boolean `True` or `False`).
  * Key trait: Stores only values with $\mathcal{O}(1)$ average existence verification without extra overhead.

* Single-Pass Complement Hash Map (`dict`):
  * Use case: When you need to retrieve or reference an associated value linked to that element (such as an index, seen count, or position).
  * Key trait: Maps a complement or target value to its corresponding metadata dynamically in a single pass.
