# Day 2 — Self-Learning Log

---

## Daily Agenda

* LeetCode Practice
  * #217 — Contains Duplicate
  * #680 — Valid Palindrome II
* Core Study Topics
  * Core Focus: Character frequency counting via fixed 26-element array vs. hash table
  * Secondary: PCAP (Certified Associate in Python Programming) Exam Prep (Module 2)
* Production Code
  * Initialize Project 1
  * Research and plan implementation for Part 1 of Project 1

---

## Summary & Completed Tasks

* LeetCode: Completed problems with full documentation and solution READMEs.
* Project Development: Successfully created and initialized Project 1 repository/directory.

---

## Key Learning Outcomes

### 1. Data Structures & Algorithms (LeetCode)
* Fixed-Size Arrays: Utilizing fixed-length arrays (e.g., size 26) mapped by character offset (`ord(c) - ord('a')`) for efficient frequency counting.

### 2. Python Fundamentals (PCAP Prep - Module 2)
* Character Encoding Standards: ASCII, Unicode, UTF-8, and internal representation.
* Nature of Strings: Immutability, slicing behavior, indexing, and built-in methods.
* Exceptions & Error Handling: Try/except blocks, custom exceptions, raising exceptions, and cleanup routines.

### 3. Production Code Architecture
* Structural Standards: Establishing scalable directory layouts and separation of concerns.
* Environment & Tooling: Managing application configurations, dependencies, and formatting/linting tooling.

---

## Core Daily Question

> Q: When should you use character frequency counting via a fixed 26-element array vs. a hash table?

* Fixed 26-Element Array:
  * Best for: Constrained character sets (e.g., exclusively lowercase `a`-`z` or uppercase `A`-`Z`).
  * Advantages: 
    * Guarantees strict $\mathcal{O}(1)$ space complexity (specifically bounded at 26 elements).
    * Avoids hash function overhead and collision-resolution logic.
    * Offers better cache locality and faster direct indexing via character offset (`ord(c) - ord('a')`).

* Hash Table (`dict` / `Counter`):
  * Best for: Open-ended character sets (Unicode, mixed-case, whitespace, punctuation, numbers).
  * Advantages: Dynamically adapts to any key type without needing prior knowledge of the alphabet size.
