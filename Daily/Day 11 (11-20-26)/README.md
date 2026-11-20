# Day 11 - Self Learning Log

## Agenda

### LeetCode
* **#643** Maximum Average Subarray I
* **#1343** Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

### Learning
* **Core Focus:** Fixed window template of length $k$; maintaining a running sum without re-summing slices.
* **Secondary Focus:** AWS-Dev (Course 2)

### Production Code
* **Project 1:** Backend development (Request Bodies)

---

## Conclusion

### Completed
* LeetCode problems with full `README.md` documentation
* Project 1: Backend development (Request Bodies)

### Learning Outcomes
* **AWS-Dev (Course 2):**
  * The cloud-native developer mindset
  * Evaluating AWS compute platforms and tradeoffs
  * Core cloud-native design principles
  * AI-assisted cloud development on AWS
  * Key exam and best-practice takeaways
* **Production Code (Setting up Request Bodies):**
  * Definition of a request body
  * When to use it
  * How to define the exact shape
  * Architecture breakdown for Project 1

---

## Core Daily Question

**What is a fixed window template of length $k$ while maintaining a running sum without re-summing slices?**

### Fixed Window Running Sum Template

```python
# 1. Compute the first window's sum once (indices 0 to k - 1)
window_sum = sum(arr[:k])

# 2. Record the result for that initial window
# [Problem-specific logic goes here]

# 3. Slide the window one step at a time from index k to n - 1
for i in range(k, len(arr)):
    # Add incoming right element (arr[i])
    # Subtract outgoing left element (arr[i - k])
    window_sum += arr[i] - arr[i - k]
    
    # Update the result for the new window
    # [Problem-specific logic goes here]
```
