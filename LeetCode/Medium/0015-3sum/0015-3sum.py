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



        