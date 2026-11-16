class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        combinations = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue #skips duplicates
            left = i + 1
            right = len(nums) - 1

            while left < right:
                added = nums[i] + nums[left] + nums[right]
                if added == 0:
                    combinations.append([nums[i], nums[left], nums[right]])

                    #skipping duplicate left and right values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    #moving pointers inward to look for pairs
                    left += 1
                    right -= 1

                elif added > 0:
                    right -= 1
                else:
                    left += 1
        
        return combinations


"""
Time complexity: 
    - O(n^2) in the worst case. The outer loop runs n times, and for each i, the two-pointer inner loop traverses the remainder of the array once, leading to roughly n + (n-1) + ... = O(n^2).

Space complexity: 
    - O(1) extra space beyond the output. The algorithm sorts in place (in-place sort might use O(log n) recursion stack for quicksort/mergesort depending on implementation), and uses a few pointers and a result list. If counting the output, space is O(k) where k is the number of triplets found.
"""


        
