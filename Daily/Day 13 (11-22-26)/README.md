# Day 13 — Self-Learning Log

## Agenda

| Category | Focus Areas |
| :--- | :--- |
| **LeetCode** | • **#3** Longest Substring Without Repeating Characters<br>• **#424** Longest Repeating Character Replacement |
| **Core Learning** | Tracking character sets in dynamic windows; tracking max frequency count to test window validity |
| **Secondary Learning** | AWS-Dev (Course 4) |
| **Production Code** | **Project 1:** Backend Development (API Versioning) |

---

## Conclusion & Progress

### Completed Tasks
- [x] **LeetCode:** Solved #3 & #424 with full READMEs
- [x] **Project 1:** Backend Development (API Versioning)

### Key Learning Outcomes

#### AWS-Dev — Course 4
* Core DynamoDB Hierarchy and Primary Keys
* Secondary Indexes: LSI vs. GSI
* Reading and Writing Data via the SDK (CRUD)
* Capacity Models, TTL, and DynamoDB Streams
* Key Exam and Best-Practice Takeaways

#### Production Code — Setting Up API Versioning
* API Versioning definition
* Architecture Breakdown for Project 1

---

## Core Daily Question

> **What is tracking character sets in dynamic windows and tracking max frequency count to test window validity?**

### 1. Tracking Character Sets in a Dynamic Window
**The Mechanics — The "Expand-Until-Conflict" Loop**  
Think of the `right` pointer as the **explorer** and the `left` pointer as the **cleanup crew**:

1. **Expand (`right` moves right):** The explorer tries to step onto `s[right]`.
2. **Conflict Check:** Before accepting `s[right]`, check the `Set`. If `s[right]` is already in the `Set`, adding it would violate the uniqueness rule.
3. **Contract (`left` moves right):** The cleanup crew advances `left`, deleting `s[left]` from the `Set` at every step until the previous copy of `s[right]` is evicted.
4. **Commit:** Now that the conflict is cleared, add the new `s[right]` to the `Set` and record the window's size (`right - left + 1`).

---

### 2. Tracking Max Frequency Count (Majority Rule)

* **The Rule:** You can replace at most `k` characters to make the entire window consist of a single repeating character.
* **The State:**
  * **`counts`:** A frequency map tracking the occurrences of characters in the current window.
  * **`max_freq`:** A single integer tracking the highest count of any single character seen in a window.
* **Shrinking Behavior:** When the window becomes invalid, shift `left` forward by `1` (decrementing `counts[s[left]]`).

#### Window Validity Formula
To make all characters in a window of size `window_len` identical, keep the most frequent character and replace everything else:

$$\text{Replacements Needed} = \text{window\_len} - \text{max\_freq}$$

| Window State | Condition | Action |
| :--- | :--- | :--- |
| **Valid Window** | $(\text{right} - \text{left} + 1) - \text{max\_freq} \le k$ | Keep expanding `right` and record max length |
| **Invalid Window** | $(\text{right} - \text{left} + 1) - \text{max\_freq} > k$ | Shift `left` forward by `1` and decrement `counts[s[left]]` |
