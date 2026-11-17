# Day 8 - Self-Learning Log

## Agenda

### LeetCode
* **#56:** Merge Intervals
* **#57:** Insert Interval

### Learning Focus
* **Core Focus:** Interval boundary comparison; maintaining a dynamic merged output buffer
* **Secondary Focus:** PCAP studying (Module 3 - Review)

### Production Code
* **Project 1:** Backend development (building HTTP methods)

---

## Conclusion

### Completed
* LeetCode problems (#56 and #57) with full READMEs
* Project 1: Backend development (HTTP methods)

### Learning Outcomes
* **PCAP Studying:** Module 3 (4 core pillars of OOP)
* **Production Code:** Setting up HTTP methods (5 core methods, safety, and idempotency)

---

## Core Daily Question

**Q: What is interval boundary comparison while maintaining a dynamic merged output buffer?**

> **A:** Assuming the intervals are sorted by their start times, you take the end of the last interval in your merged buffer (the first value) and the start of the current interval (the second value) and compare them. 
> 
> * **If they overlap** (`current_start <= last_merged_end`): You update the interval in the merged buffer to keep the start of the first interval and take `max(both ends)` as the new end boundary.
> * **If they don't overlap:** You append the entirety of the second interval to the merged buffer as a new entry. 
> 
> This dynamic buffer approach allows you to resolve chain-overlapping intervals in a single linear pass ($O(n)$) after sorting.
