class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        #dynamic expansion: grow window until sum >= target
        for right in range(len(nums)):
            current_sum += nums[right]

            #greedy contraction: shrink as much as possible while still valid
            while current_sum >= target:
                #records answer before shrinkage breaks the valid condition
                min_length = min(min_length, right - left + 1)

                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0


"""
Time complexity: 
    - O(n), where n is the length of nums. Each element is added to the window once (right increases) and removed at most once (left increases), so the total number of operations is linear.

Space complexity: 
    - O(1), excluding the input storage. The algorithm uses a fixed number of variables.
"""   