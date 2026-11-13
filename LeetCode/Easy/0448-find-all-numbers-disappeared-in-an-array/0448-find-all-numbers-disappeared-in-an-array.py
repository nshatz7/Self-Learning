class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        disappear = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                disappear.append(i + 1)
            

        return disappear


        

            
            
            
        

        
        
        