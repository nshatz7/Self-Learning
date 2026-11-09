class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)): #check if the orginial list is long than the set of unique characters (which if it is, means that when converting to set it removed a duplicate)
            return True
        
        return False #if it couldn't find a duplicate after going through the WHOLE loop

    #Time complexity: O(n) on average, where n is the length of nums. Building the set takes O(n) time and comparing lengths is O(1). Overall still O(n).
    #Space complexity: O(n) in the worst case, since the set may store all n unique elements.

        

 
        
