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

"""
Time complexity:
- The algorithm solves the kSum problem recursively. In the worst case, it explores combinations of k numbers from n elements. The number of k-combinations is O(n choose k), and at each level some overhead occurs (sorting initially is O(n log n)).
- For 4Sum, k is 4, so the dominant term is roughly O(n^3) in the worst case, due to three nested levels of iteration after fixing the first element (e.g., i, then recursive kSum with k-1). The two-pointer base case for k = 2 runs in O(n) for each recursive call.
- Overall time is O(n^3) in the typical worst case with duplicates removal and pruning, plus the initial sort O(n log n). In sparse or pruned inputs, it can be better.

Space complexity:
- The algorithm uses extra space for the result storage. In the worst case, the number of found quadruplets can be O(n^4) in pathological inputs, but typically much less; the storage for the result dominates.
- Additional auxiliary space: the recursion depth is 3 (for k=4, it recurses down to k=2), so the call stack O(k) = O(4) = O(1) auxiliary space. The two-pointer base case uses O(1) extra space. Overall auxiliary space is O(1) aside from the output.
"""



        
        
