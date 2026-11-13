class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0 #intializing int for holding the longest count

        if len(nums) == 0: #stopping right away if there are no elemnts in nums and returning 0
            return longest

        nums_set = set(nums) #turning nums into a set to remove duplicates
        for num in nums_set:
            if (num - 1) not in nums_set: #if 'nums' is a streak root or start of a sequence (ex: 1, 2, 3, 5; 5 - 1 = 4; 5 must be the start of a new sequence)
                current_num = num #adding a new value we can add to in our while loop
                count = 1 #new int to count the length of the sequence before making it the longest
                while (current_num + 1) in nums_set: #if its consecutive and the next number is still in nums_set then keep going
                    current_num += 1 #adding the next number to continue the loop
                    count += 1 #if still in while then the count of the sequence length must go up
                longest = max(longest, count) #comparing if longest > count or count > longest, and setting longest to the bigger one
        
        return longest #once finished with all numbers in nums, return the longest sequence length


"""
Time complexity: 
    - O(n) on average. Each number is processed as a potential start of a sequence at most once, and the inner while traverses each element of a consecutive run exactly once overall. In the worst case with n distinct numbers forming one long sequence, the inner loop runs n-1 times total. The set lookups are O(1) on average.

Space complexity: 
    - O(n) for storing the set of numbers. Additional variables use O(1) extra space.
"""
        
            
        
