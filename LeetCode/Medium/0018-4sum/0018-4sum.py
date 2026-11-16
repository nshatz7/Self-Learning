class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = self.kSum(0, 4, target ,nums)

        return result


    def kSum(self, start, k, target, nums): #start: lowest index available, k: how many #'s still need to be chosen, target: remaining sum required
        holder = []

        #early-exit conditions
        if start >= len(nums) or len(nums) - start < k: 
            return []
        avg = target // k
        if nums[start] > avg or nums[-1] < avg:
            return []

        if k == 2: #base case where k == 2
            left = start
            right = len(nums) - 1
            while left < right:
                curr = nums[left] + nums[right]
                if curr < target:
                    left += 1
                elif curr > target:
                    right -= 1
                else: #curr == target (it works)
                    holder.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            return holder

        for i in range(start, len(nums) - k + 1): #inclusive
            if i > start and nums[i] == nums[i - 1]: #skipping duplicates
                continue
            for subset in self.kSum(i + 1, k - 1, target - nums[i], nums): #reducing problem recursively
                holder.append([nums[i]] + subset) #turns nums[i] into a list and concatenates

        return holder





        
        