class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        
        return False #if it couldn't find a duplicate after going through the WHOLE loop

        """
        what I learned:
        - Using two nested loops results in a time complexity of o(n^2). This is an issue because for large data sets this takes a long amount of time for something simple.
            -To fix this, use Python data structures that let you test for exisistence with o(1) constant:
                - set (checks if an item exists, what I used in this problem)
                - dict (looks up a value via a key)
        - For loops automatically make the overall function o(n) linear automatically, but loops are sometimes NEEDED for functions (eg. analyzing specific values in a array (not here because we don't care for the actual value, we just care if it was repeated))
        - When a list containing duplicates is converted to a set, all duplicate items are automatically removed in Python, leaving only a collection of unique items.
            -To convert a list to a set:
                my_list = set(my_list)
        - You don't always have to trade off time and space complexity, but "time-space trade-off" is very common

        """

        

 
        