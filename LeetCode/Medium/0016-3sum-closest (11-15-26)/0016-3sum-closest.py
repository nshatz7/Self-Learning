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


"""
Time complexity: 
    - O(n^2) in the worst case. After sorting (O(n log n)), the two-pointer scanning runs for each i (up to n) with left/right pointers moving at most n steps in total per i, giving O(n^2).

Space complexity: 
    - O(1) extra space (ignoring the input array and the sorting that may require O(n) auxiliary space depending on the sort implementation; otherwise the algorithm uses a constant amount of extra variables).
"""
                

        
