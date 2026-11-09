class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        else:
            return False

        """
        what I learned:
        - Using two nested loops results in a time complexity of o(n^2). This is an issue because for large data sets this takes a long amount of time for something simple.
            -To fix this, use Python data structures that let you test for exisistence with o(1) constant:
                - set (checks if an item exists, what I used in this problem)
                - dict (looks up a value via a key)
        """

        

 
        