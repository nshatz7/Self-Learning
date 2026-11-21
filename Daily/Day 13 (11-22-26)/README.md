Day 13 - Self learning log

Agenda
Leetcode:
- #3 Longest Substring Without Repeating Characters
- #424 Longest Repeating Character Replacement
Learning:
- Core Focus: Tracking character sets in dynamic windows; tracking max frequency count to test window validity.
- Secondary Focus: AWS-Dev (course 4)
Production Code:
- Project 1: Backend Development (API Versioning)

Conclusion
Completed:
- LeetCode problems with full README's
- Project 1: BAckend Development (API Versioning)
Learning Outcomes:
- AWS-Dev: course 4 (Core DynamoDB Hierarchy and Primary Keys; Secondary Indexes: LSI vs. GSI; Reading and Writing Data Via the SDK (CRUD); Capacity Models, TTL, and DynamoDB Streams; Key Exam and Best-Practice Takeaways)
- Production Code: Setting Up API Versioning (API Versioning definition, Architecture Breakdown for Project 1)
Core Daily Question: What is tracking character sets in dynamic windows and tracking max frequency count to test window validity?
- Tracking Character Sets in a Dynamic Window:
    The Mechanics: The "Expand-Until-Conflict" Loop Think of the right pointer as the explorer and the left pointer as the cleanup crew:
    
    Expand (right moves right): The explorer tries to step onto s[right].
    Conflict Check: Before accepting s[right], check the Set. If s[right] is already in the Set, adding it would violate the uniqueness rule.
    Contract (left moves right): The cleanup crew advances left, deleting s[left] from the Set at every step until the previous copy of s[right] is evicted.
    Commit: Now that the conflict is cleared, add the new s[right] to the Set and record the window's size (right - left + 1).
- 


