# Day 14 — Self-Learning Log

## Agenda

| Category | Focus Areas |
| :--- | :--- |
| **LeetCode** | • **#567** Permutation in String<br>• **#438** Find All Anagrams in a String |
| **Core Learning** | Fixed sliding window over character frequency maps; maintaining a `matches` counter to avoid $O(26)$ scans |
| **Secondary Learning** | AWS-Dev (Course 5) |
| **Production Code** | **Project 1:** Backend Development (Dependency Injection) |

---

## Conclusion & Progress

### Completed Tasks
- [x] **LeetCode:** Solved #567 & #438 with full READMEs
- [x] **Project 1:** Backend Development (Dependency Injection)

### Key Learning Outcomes

#### AWS-Dev — Course 5
* Local Testing with the AWS SAM CLI
* How AWS Lambda Handles Errors by Invocation
* Dead-Letter Queues (DLQs) vs. Lambda Destinations
* API Gateway Request Validation and Error Mapping
* Key Exam and Best-Practice Takeaways

#### Production Code — Setting Up Dependency Injection
* Dependency Injection definition
* Architecture Breakdown for Project 1

---

## Core Daily Question

> **What is a fixed sliding window over character frequency maps while maintaining a `matches` counter to avoid $O(26)$ scans?**

### 1. Fixed Sliding Window
* **Definition:** A contiguous subarray or substring of a locked length $k$ (where $k = \text{s1.length}$) that moves across a sequence one step at a time from left to right.
* **Application:** Since any permutation of `s1` must have the exact same length as `s1`, we only need to inspect windows of size `s1.length` inside `s2`. As the window slides right by one character, we add the new character entering from the right and remove the old character exiting from the left.

---

### 2. Array-Based Character Frequency Map
* **Definition:** When working exclusively with lowercase English letters (`'a'` through `'z'`), we can use a fixed-size array of 26 integers (`'a' = 0`, `'b' = 1`, ..., `'z' = 25`) instead of a standard hash map.
* **Application:** Provides true $O(1)$ lookups, insertions, and space complexity ($O(26) \rightarrow O(1)$), avoiding the memory overhead and hashing collisions of a dynamic dictionary/hash map.

---

### 3. Maintaining the `matches` Counter
* **Definition:** A single integer variable that tracks how many of the 26 alphabet buckets currently have identical character frequencies in both `s1` and the current window of `s2`.
* **Application:** Eliminates the need to scan and compare all 26 buckets at every step of the sliding window. When `matches == 26`, every character frequency aligns, meaning we have found a valid permutation in $O(1)$ check time.
