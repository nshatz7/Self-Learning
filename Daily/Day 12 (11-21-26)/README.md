# Day 12 - Self Learning Log

## Agenda

### LeetCode
* **#209** Minimum Size Subarray Sum
* **#1004** Max Consecutive Ones III

### Learning
* **Core Focus:** Dynamic window expansion (`right += 1`) and greedy contraction (`left += 1`) to hit numeric thresholds.
* **Secondary Focus:** AWS-Dev (Course 3)

### Production Code
* **Project 1:** Backend development (Response models)

---

## Conclusion

### Completed
* LeetCode problems with full READMEs
* **Project 1:** Backend development (Response models)

### Learning Outcomes
* **AWS-Dev (Course 3):**
  * End-to-end request lifecycle
  * Anatomy of an AWS Lambda function
  * Amazon API Gateway: API types and integrations
  * Stages, deployments, and CORS
  * Defining an API with AWS SAM
  * Key exam and best-practices takeaways
* **Production Code (Setting up Response Models):**
  * Definition of a response model and its purpose
  * Architecture breakdown for Project 1

---

## Core Daily Question
**What is dynamic window expansion (`right += 1`) and greedy contraction (`left += 1`) to hit numeric thresholds?**

### 1. Dynamic Expansion (`right += 1`)
* Move the `right` pointer forward to ingest new elements and update a running state (e.g., `current_sum`).
* Keep expanding until a specific numeric threshold is either met or broken (e.g., `current_sum >= target`).

### 2. Greedy Contraction (`left += 1`)
* Once the threshold triggers, advance the `left` pointer to shrink the window from the back.
* Strip away old elements and update the running state (e.g., `current_sum -= nums[left]`) until the condition flips back (e.g., `current_sum < target`).

### 3. When to Record the Answer
The subtle trick lies in *when* you update your best answer, which depends entirely on whether the problem asks for a minimum or maximum subarray:
* **Minimum Subarray (This Problem):** Record the answer **inside** the contraction `while` loop, because every valid step while shrinking yields a potentially smaller, valid window.
* **Maximum Subarray:** Record the answer **outside (after)** the contraction `while` loop, once the window has been restored to a valid state.
