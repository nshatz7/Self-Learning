class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for y in range (i + 1, len(nums)):
                combinations = nums[i] + nums[y]
                if combinations == target:
                    return(i, y,)

        
        