class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        disappear = [] #array of numbers that are not in nums
        for num in nums:
            index = abs(num) - 1 #index correlated to the number in nums. abs() for the next if statement because a negative numbers index isn't negative
            if nums[index] > 0: #checking if that number was already converted to negative and skipping if so (no repeat converting a negative number to positive)
                nums[index] *= -1 #in-place array sign marking 
        
        for i in range(len(nums)):
            if nums[i] > 0: #if the value at the index is greater than 0, we didn't see it in the first loop so it has to be missing. We know nums has that index though because of the constraints of the problem saying that n == nums.length, meaning that it still has an index for a missing value
                disappear.append(i + 1) #add missing value to disappear list
            

        return disappear #return the list of missing numbers


"""
Time complexity: 
    - O(n), where n is the length of nums. The algorithm makes a single pass to mark seen numbers and a second pass to collect disappeared numbers.

Space complexity: 
    - O(1) extra space (excluding the output list). It uses the input array in place for marking and only stores the result.
"""


        

            
            
            
        

        
        
        
