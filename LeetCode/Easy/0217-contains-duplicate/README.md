Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

what I learned:
        - Using two nested loops results in a time complexity of o(n^2). This is an issue because for large data sets this takes a long amount of time for something simple.
            -To fix this, use Python data structures that let you test for exisistence with o(1) constant:
                - set (checks if an item exists, what I used in this problem)
                - dict (looks up a value via a key)
        - For loops automatically make the overall function o(n) linear automatically, but loops are sometimes NEEDED for functions (eg. analyzing specific values in a array (not here because we don't care for the actual value, we just care if it was repeated))
        - When a list containing duplicates is converted to a set, all duplicate items are automatically removed in Python, leaving only a collection of unique items.
            -To convert a list to a set:
                my_list = set(my_list)
        - You don't always have to trade off time and space complexity, but "time-space trade-off" is very common
				- Conditional for duplicate problems (common on interviews):
						- Standard safe choices (prioritize in this problem because they make fewer assumptions on vague data):
								- Hash sets: Excellent time complexity (o(n)), high space complexity (o(n)), unbalanced (fast moving, but have a poor memory score)
								- Sorting: Good time complexity (o(nlogn)), low space complexity (o(logn)), balanced (good memory score and acceptable runtime)
						- Alternatives:
								- The "index marking" technique (sometimes looked for in coding interviews)
								- Bit Vector / BitSet
						- When to use them:
								- Hash set or sorting: Small lists or huge range (e.g. 64 bit ID or sparse data)
								- Bit Vector: Millions of 32-bit ints (have dense data and/or known boundaries)
								- The "index marking" technique: The problem guarantees every number is within the range of the arrays length (e.g. [1, 2, 2] (largest and smallest is between 0 and 3)) (if the numbers are randomly distributed across a massive range, floats, or negatives: index marking doesn't work)
		
