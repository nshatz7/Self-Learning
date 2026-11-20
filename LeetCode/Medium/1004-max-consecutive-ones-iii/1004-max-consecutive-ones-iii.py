class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            #dynamic window expansion: include nums[right] in window
            if nums[right] == 0:
                zero_count += 1
            
            #numeric threshold and greedy contraction: shrink from the left until the window has at most k zeros again
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            #record result: window is gauranteed valid here
            max_length = max(max_length, right - left + 1)

        return max_length
        

"""
Time complexity: 
    - O(n), where n is the length of nums. Each index is visited at most once by the right pointer and at most once by the left pointer inside the while loop.

Space complexity: 
    - O(1), aside from input storage, since only a few integer counters are used.
"""