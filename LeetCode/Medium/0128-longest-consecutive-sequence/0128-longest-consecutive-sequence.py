class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0

        if len(nums) == 0:
            return longest

        nums_set = set(nums)
        for num in nums_set:
            if (num - 1) not in nums_set:
                current_num = num
                count = 1
                while (current_num + 1) in nums_set:
                    current_num += 1
                    count += 1
                longest = max(longest, count)
        
        return longest
        
            
        