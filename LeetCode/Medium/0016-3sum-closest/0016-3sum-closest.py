class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue #skips duplicates
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                added = nums[i] + nums[left] + nums[right]
                if abs(target - added) < abs(target - closest):
                    closest = added

                if added < target:
                    left += 1
                elif added > target:
                    right -= 1
                else:
                    return added #exact match found

        return closest


                

        