# Systems, Algorithms & Cloud Architecture — Engineering Log

> *"First, solve the problem. Then, write the code."*

This repository is a living logbook of my work across computer science fundamentals, algorithmic problem-solving, and cloud architecture. 

Rather than dumping raw code or chasing a high problem count, this repo is built around **first-principles understanding**. Every solution, course module, and architectural diagram here includes written breakdowns of *why* an approach works, the time and space trade-offs involved, and what broke along the way.

---

## Repository Architecture

```text
.
├── daily/                  # Day-to-day engineering logs and scratchpad code
│   └── YYYY-MM-DD/         # Daily directories with agendas, notes, and takeaways
├── leetcode/               # Algorithmic problem-solving
│   ├── easy/
│   ├── medium/
│   └── hard/               # Each problem includes a README covering approach & complexity
├── courses/                # Structured computer science coursework
│   └── mit-6.0001/         # Problem sets, lecture notes, and implementations
└── production-projects/    # End-to-end systems and backend services
    ├── lead-management-api/
    └── [project-02]/

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [0015-3sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0015-3sum/) | Medium |
| [0016-3sum-closest](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0016-3sum-closest/) | Medium |
| [0018-4sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0018-4sum/) | Medium |
| [0056-merge-intervals](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0056-merge-intervals/) | Medium |
| [0057-insert-interval](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0057-insert-interval/) | Medium |
| [0075-sort-colors](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0075-sort-colors/) | Medium |
| [0150-evaluate-reverse-polish-notation](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0150-evaluate-reverse-polish-notation/) | Medium |
| [0209-minimum-size-subarray-sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0209-minimum-size-subarray-sum/) | Medium |
| [0239-sliding-window-maximum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0239-sliding-window-maximum/) | Hard |
| [0643-maximum-average-subarray-i](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0643-maximum-average-subarray-i/) | Easy |
| [0739-daily-temperatures](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0739-daily-temperatures/) | Medium |
| [1004-max-consecutive-ones-iii](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/1004-max-consecutive-ones-iii/) | Medium |
| [1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Medium |
## Two Pointers
| Problem Name | Difficulty |
| ------- | ------- |
| [0015-3sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0015-3sum/) | Medium |
| [0016-3sum-closest](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0016-3sum-closest/) | Medium |
| [0018-4sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0018-4sum/) | Medium |
| [0075-sort-colors](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0075-sort-colors/) | Medium |
| [0567-permutation-in-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0567-permutation-in-string/) | Medium |
## Sorting
| Problem Name | Difficulty |
| ------- | ------- |
| [0015-3sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0015-3sum/) | Medium |
| [0016-3sum-closest](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0016-3sum-closest/) | Medium |
| [0018-4sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0018-4sum/) | Medium |
| [0056-merge-intervals](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0056-merge-intervals/) | Medium |
| [0075-sort-colors](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0075-sort-colors/) | Medium |
## Quicksort
| Problem Name | Difficulty |
| ------- | ------- |
| [0056-merge-intervals](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0056-merge-intervals/) | Medium |
| [0075-sort-colors](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0075-sort-colors/) | Medium |
## Bubble Sort
| Problem Name | Difficulty |
| ------- | ------- |
| [0075-sort-colors](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0075-sort-colors/) | Medium |
## String
| Problem Name | Difficulty |
| ------- | ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0003-longest-substring-without-repeating-characters/) | Medium |
| [0020-valid-parentheses](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0020-valid-parentheses/) | Easy |
| [0076-minimum-window-substring](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0076-minimum-window-substring/) | Hard |
| [0424-longest-repeating-character-replacement](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0424-longest-repeating-character-replacement/) | Medium |
| [0438-find-all-anagrams-in-a-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0438-find-all-anagrams-in-a-string/) | Medium |
| [0567-permutation-in-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0567-permutation-in-string/) | Medium |
## Stack
| Problem Name | Difficulty |
| ------- | ------- |
| [0020-valid-parentheses](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0020-valid-parentheses/) | Easy |
| [0150-evaluate-reverse-polish-notation](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0150-evaluate-reverse-polish-notation/) | Medium |
| [0155-min-stack](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0155-min-stack/) | Medium |
| [0739-daily-temperatures](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0739-daily-temperatures/) | Medium |
## Bracket Sequences
| Problem Name | Difficulty |
| ------- | ------- |
| [0020-valid-parentheses](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0020-valid-parentheses/) | Easy |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [0150-evaluate-reverse-polish-notation](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0150-evaluate-reverse-polish-notation/) | Medium |
## Design
| Problem Name | Difficulty |
| ------- | ------- |
| [0155-min-stack](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0155-min-stack/) | Medium |
## Monotonic Stack
| Problem Name | Difficulty |
| ------- | ------- |
| [0739-daily-temperatures](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0739-daily-temperatures/) | Medium |
## Sliding Window
| Problem Name | Difficulty |
| ------- | ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0003-longest-substring-without-repeating-characters/) | Medium |
| [0076-minimum-window-substring](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0076-minimum-window-substring/) | Hard |
| [0209-minimum-size-subarray-sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0209-minimum-size-subarray-sum/) | Medium |
| [0239-sliding-window-maximum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0239-sliding-window-maximum/) | Hard |
| [0424-longest-repeating-character-replacement](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0424-longest-repeating-character-replacement/) | Medium |
| [0438-find-all-anagrams-in-a-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0438-find-all-anagrams-in-a-string/) | Medium |
| [0567-permutation-in-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0567-permutation-in-string/) | Medium |
| [0643-maximum-average-subarray-i](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0643-maximum-average-subarray-i/) | Easy |
| [1004-max-consecutive-ones-iii](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/1004-max-consecutive-ones-iii/) | Medium |
| [1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Medium |
## Binary Search
| Problem Name | Difficulty |
| ------- | ------- |
| [0209-minimum-size-subarray-sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0209-minimum-size-subarray-sum/) | Medium |
| [1004-max-consecutive-ones-iii](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/1004-max-consecutive-ones-iii/) | Medium |
## Prefix Sum
| Problem Name | Difficulty |
| ------- | ------- |
| [0209-minimum-size-subarray-sum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0209-minimum-size-subarray-sum/) | Medium |
| [1004-max-consecutive-ones-iii](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/1004-max-consecutive-ones-iii/) | Medium |
## Hash Table
| Problem Name | Difficulty |
| ------- | ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0003-longest-substring-without-repeating-characters/) | Medium |
| [0076-minimum-window-substring](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0076-minimum-window-substring/) | Hard |
| [0424-longest-repeating-character-replacement](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0424-longest-repeating-character-replacement/) | Medium |
| [0438-find-all-anagrams-in-a-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0438-find-all-anagrams-in-a-string/) | Medium |
| [0567-permutation-in-string](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0567-permutation-in-string/) | Medium |
## Queue
| Problem Name | Difficulty |
| ------- | ------- |
| [0239-sliding-window-maximum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0239-sliding-window-maximum/) | Hard |
## Heap (Priority Queue)
| Problem Name | Difficulty |
| ------- | ------- |
| [0239-sliding-window-maximum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0239-sliding-window-maximum/) | Hard |
## Monotonic Queue
| Problem Name | Difficulty |
| ------- | ------- |
| [0239-sliding-window-maximum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0239-sliding-window-maximum/) | Hard |
## Range Minimum/Maximum Query
| Problem Name | Difficulty |
| ------- | ------- |
| [0239-sliding-window-maximum](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Hard/0239-sliding-window-maximum/) | Hard |
## Linked List
| Problem Name | Difficulty |
| ------- | ------- |
| [0021-merge-two-sorted-lists](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0021-merge-two-sorted-lists/) | Easy |
| [0092-reverse-linked-list-ii](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Medium/0092-reverse-linked-list-ii/) | Medium |
| [0206-reverse-linked-list](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0206-reverse-linked-list/) | Easy |
## Recursion
| Problem Name | Difficulty |
| ------- | ------- |
| [0021-merge-two-sorted-lists](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0021-merge-two-sorted-lists/) | Easy |
| [0206-reverse-linked-list](https://github.com/nshatz7/Self-Learning/tree/main/LeetCode/Easy/0206-reverse-linked-list/) | Easy |
<!---LeetCode Topics End-->