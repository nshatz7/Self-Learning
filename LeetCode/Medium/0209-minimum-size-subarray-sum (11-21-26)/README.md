# 209. Minimum Size Subarray Sum

## Problem Statement
Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### Examples

* **Example 1:**
  * **Input:** `target = 7`, `nums = [2,3,1,2,4,3]`
  * **Output:** `2`
  * **Explanation:** The subarray `[4,3]` has the minimal length under the problem constraint.

* **Example 2:**
  * **Input:** `target = 4`, `nums = [1,4,4]`
  * **Output:** `1`

* **Example 3:**
  * **Input:** `target = 11`, `nums = [1,1,1,1,1,1,1,1]`
  * **Output:** `0`

### Constraints
* $1 \le \text{target} \le 10^9$
* $1 \le \text{nums.length} \le 10^5$
* $1 \le \text{nums}[i] \le 10^4$

---

## Key Takeaways & Pattern: Sliding Window

This problem is a classic application of a variable-size **Sliding Window** using **dynamic expansion** and **greedy contraction**.

### 1. Dynamic Expansion (`right += 1`)
* Move the `right` pointer forward to ingest new elements and update a running state (e.g., `current_sum`).
* Keep expanding until a specific numeric threshold is either met or broken (`current_sum >= target`).

### 2. Greedy Contraction (`left += 1`)
* Once the threshold triggers, advance the `left` pointer to shrink the window from the back.
* Strip away old elements and update the running state (`current_sum -= nums[left]`) until the condition flips back (`current_sum < target`).

### 3. When to Record the Answer
* The subtle trick lies in **when** you update your best answer, which depends entirely on whether the problem asks for a **minimum** or **maximum** subarray:
  * **Minimum Subarray (This Problem):** Record the answer **inside** the contraction `while` loop, because every valid step while shrinking yields a potentially smaller, valid window.
  * **Maximum Subarray:** Record the answer **outside** (after) the contraction `while` loop, once the window has been restored to a valid state.

